import secrets
CHARSET_DEFAULT :str ='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

#! NOPE
# def base62_encode(deci) -> str:
#     s:str = CHARSET_DEFAULT
#     hash_str:str = ''
#     while deci > 0:
#         hash_str = s[deci % 62] + hash_str
#         deci = int( (deci /62) * 100)
#     return hash_str

def create_secret_key() -> str :
   """
   Creates and returns a Random str of len 7.
   :rtype: str
   """ 
   return "".join(secrets.choice(CHARSET_DEFAULT) for _ in range(7))