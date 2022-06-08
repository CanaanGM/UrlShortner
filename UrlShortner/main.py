from fastapi import FastAPI, Depends, Request
from fastapi.responses import RedirectResponse
import validators
from sqlalchemy.orm import Session

from . import schemas, models, database, helpers

from UrlShortner.error_handling import raise_bad_request, raise_not_found

app = FastAPI()

@app.get("/")
def read_root():
    return {
        "/": "You are here, you could try /docs",
        "url":"POST - create short url",
        "/<url key>":"get redirected to the url u've shortened"
        }

database.Base.metadata.create_all(bind=database.engine)
def get_db():

    db = database.SessionLocal()

    try:

        yield db

    finally:

        db.close()



@app.post("/url", response_model=schemas.URLInfo)
def create_url(url: schemas.URLBase, db: Session = Depends(get_db)):

    if not validators.url(url.target_url):
        raise_bad_request(message="Provided URL isn't valid!")

    key:str = helpers.create_secret_key()

    try:

        db_url = models.URL(target_url=url.target_url, key=key)

        db.add(db_url)

        db.commit()

        db.refresh(db_url)

        db_url.url = key
    except Exception as ex:
        raise (ex)
    return db_url


@app.get("/{url_key}")
def forward_to_target_url(
    url_key: str, request: Request, db: Session = Depends(get_db)
):

    db_url = db.query(models.URL).filter(models.URL.key == url_key, models.URL.is_active).first()

    if db_url:

        return RedirectResponse(db_url.target_url)

    else:

        raise_not_found(request)