---
title: "Python3 - Requests Library"
keywords: 
last_updated: 
tags: 
sidebar: documentation_sidebar
permalink: Py-Requests-Library.html
folder: Scripts
---


## Basic requests
- Importing the 'requests' library

```python
import requests
```

- GET request

```python
requests.get(<URI>)
```

- POST request

```python
requests.post(<URI>,<DATA>)
```

- PUT request

```python
requests.put(<URI>,<DATA>)
```

- DELETE request

```python
requests.delete(<URI>)
```

---

## Adding custom parameters


- GET request with custom parameters

```python
payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get(<URI>, params=payload)
```
---

## Adding custom headers


- GET request with custom headers

```python
url = 'https://api.github.com/some/endpoint'
customHeaders = {'user-agent': 'my-app/0.0.1'}
r = requests.get(<URI>, headers = customHeaders)
```
---

## Read received data


- GET request with a JSON response

```python
r = requests.get('https://api.github.com/events')
jsonResponse = r.json()
print(jsonResponse[<JSONFIELD>])
```

## Source
- [Official Request Library documentation](https://requests.readthedocs.io/en/latest/user/quickstart/#make-a-request)
