# [GetYourBit.com client](https://getyourbit.com) 

This library allows you to make requests easily.

## Examples

```python
from getyourbit import Api

# create an instance
api = Api("https://ip.getyourbit.com")

# login
api.auth(admin['login'], admin['password'])

# request without scrolling
body = api.request('/me/', {'locale': 'en-US'})
print(body['data'])

# request with scrolling
result = api.scroll('/find/', {
    'size': 500
    'query': {
        'country': 'nepal'
    }
})
print(result)

# logout
api.logout()
```

## Api
### .auth(login, password, **kwargs)
Login to the API. You can get __login__ and __password__ [on the site](https://getyourbit.com) after a subscription.
You can pass through __kwargs__ any [requests](https://github.com/requests/requests) module option. 
Free services don't require authorization.
### .logout()
Logout from the API. It gives an error without authorization before.
### .request(url, data={}, **kwargs)
### .request(url, **kwargs)
Request to the API without scrolling to get data. 
It returns all response body as object.
### .scroll(url, data={}, callback=None, **kwargs)
### .scroll(url, data={}, **kwargs)
### .scroll(url, **kwargs)
Request to the API with scrolling to get data. You can pass callback to control every chunk. You will get three arguments:

* __body__ - chunk response body
* __chunkData__ - chunk data
* __fullData__ - full data by the current chunk  

It returns the full data at the end


 
