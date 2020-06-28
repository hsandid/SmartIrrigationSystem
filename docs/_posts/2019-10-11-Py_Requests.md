---
layout: post
title:  "Python3 - REQUESTS library"
---

## Basic requests
- Importing the 'requests' library

```py
import requests
```

- GET request

```py
requests.get(<URI>)
```

- POST request

```py
requests.post(<URI>,<DATA>)
```

- PUT request

```py
requests.put(<URI>,<DATA>)
```

- DELETE request

```py
requests.delete(<URI>)
```

## Adding custom parameters
- GET request with custom parameters

```py
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(<URI>, params=payload)
```

## Adding custom headers
- GET request with custom headers

```py
url = 'https://api.github.com/some/endpoint'
customHeaders = {'user-agent': 'my-app/0.0.1'}
r = requests.get(<URI>, headers = customHeaders)
```

## Read received data
- GET request with a JSON response

```py
r = requests.get('https://api.github.com/events')
jsonResponse = r.json() 
print(jsonResponse[<JSONFIELD>])
```

## Source
- https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
