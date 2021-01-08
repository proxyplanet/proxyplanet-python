# ProxyPlanet 4G Proxy API Python Library
Official Python Library for the ProxyPlanet 4G Proxy API.


This library allows programmatic interaction with the ProxyPlanet.io APIs.  
It currently supports the following features:
- 4G Proxy IP refresh
- List 4G proxies and credentials
- Dynamically generate a valid config for python-requests

## Installation

To install from source:
```
python setup.py install
```

To install using pip:
```
pip install --upgrade proxyplanet
```

## Requirements

Python 3.5+ (PyPy supported)
python-requests

## Documentation

See the ProxyPlanet API specifications, available in the API section of your [ProxyPlanet Dashboard](https://proxyplanet.io/apis).

## Usage with python-requests

Integrating a ProxyPlanet 4G Proxy with your Python application is super easy.  

The library needs to be configured with your account's secret token which is available in your [ProxyPlanet Dashboard](https://proxyplanet.io/en/login).
Set TOKEN to its value:

```python3
import proxyplanet
import requests

# Insert your ProxyPlanet API token here
TOKEN = "0011223344..."

pp = proxyplanet.Api(TOKEN)

# Fetch a new configuration from the server
cfg = pp.requests_config()

# When calling requests specify the proxies=cfg parameter
requests.get("https://example.com/", proxies=cfg)
# <Response [200]>
```
Now you can enjoy the speed and performance of a 4G Proxy while performing your scraping or botting activities.  

## Usage with ProxyPlanet Refresh API

```python3
import proxyplanet

# Insert your ProxyPlanet API token here
TOKEN = "0011223344..."

pp = proxyplanet.Api(TOKEN)

# Fetch a list of all proxies associated with the account
proxy_list = pp.list_proxies()
print(proxy_list)
# [{"http":"http://pluto.proxyplanet.io:80/","id":44555,"password":"<proxy_password>",
# "socks5":"socks5://pluto.proxyplanet.io:1080/","https":
# "https://pluto.proxyplanet.io:443/", "username":"<proxy_username>"}]
```

To request a 4G Proxy refresh:

```python3
# If only one proxy is associated with the account the proxy id parameter is optional
success = pp.refresh()
print(success)
# True

# Refresh a specific proxy using the proxy id parameter
success = pp.refresh(44555)
print(success)
# True
```

Upon a refresh request the 4G Proxy will immediately switch to a new IP address.
