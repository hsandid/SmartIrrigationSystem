---
layout: post
title:  "Python3 - REQUESTS library"
---

# Python3 - REQUESTS library
## Basic requests
- Importing the 'requests' library

```python3 
import requests
```

- GET request

```python3 
requests.get(<URI>)
```

- POST request

```python3 
requests.post(<URI>,<DATA>)
```

- PUT request

```python3 
requests.put(<URI>,<DATA>)
```

- DELETE request

```python3 
requests.delete(<URI>)
```

## Adding custom parameters
- GET request with custom parameters

```python3 
payload = {'key1': 'value1', 'key2': 'value2'}
```

```python3 
r = requests.get(<URI>, params=payload)
```

## Adding custom headers
- GET request with custom headers

```python3 
url = 'https://api.github.com/some/endpoint'
```

```python3 
customHeaders = {'user-agent': 'my-app/0.0.1'}
```

```python3 
r = requests.get(<URI>, headers = customHeaders)
```

## Read received data
- GET request with a JSON response

```python3 
r = requests.get('https://api.github.com/events')
```

```python3 
jsonResponse = r.json()
```

```python3 
print(jsonResponse[<JSONFIELD>])
```

## Source
- https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request
