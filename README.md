# UrlShortner

##  meant as a learning exercise

```mermaid
graph LR
Url[Square Rect] -- create_key {Key:Url} --> Db((Circle))
Url --> Shorten(Round Rect)
Db --> D{Rhombus}
shorten --> D
```

## Routes:

|Verp|Route|Name|
|---|---|---|
|GET|/|home|
|Post|/url|shorten Url|
|Get|/{URL KEY}| redirect|


## Classes : 

|Name|Job|Methods|
|---|---|---|
|Helpers| helpers| |
|||Create_secret_key|
|URL|model||
