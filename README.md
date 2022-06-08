# UrlShortner

##  meant as a learning exercise

```mermaid
graph LR
req((req)) --> exists{exists}
exists -- yes --> response((response))
exists -- no --> shorten[shorten] --> db((db))  
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
