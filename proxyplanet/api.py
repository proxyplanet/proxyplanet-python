import requests

PP_API_SERVER = "https://proxyplanet.io/api/v1"

class BadCredentialsException(Exception):
    pass

class NetworkException(Exception):
    pass

class ProxyNotFound(Exception):
    pass

class AmbiguousProxy(Exception):
    pass

class TooManyRefreshesException(Exception):
    pass

class Api:
    def __init__(self, token):
        self.token = token
        self.__headers = {
            "Token": self.token
        }

        # Validate token
        self.__list()

    def __find_proxy_id(self, proxy_id):
        r = self.__list()
        if proxy_id == None:
            if len(r["proxies"]) == 0:
                raise ProxyNotFound("No active 4G Proxy is associated with this account")
            if len(r["proxies"]) > 1:
                raise AmbiguousProxy("Multiple 4G Proxies are associated with this account, please select one using the proxy_id parameter")
            proxy_id = r["proxies"][0]["id"]
        if proxy_id not in [x["id"] for x in r["proxies"]]:
            raise ProxyNotFound("The specified 4G Proxy does not exist or is not associated with this account")
        return proxy_id, r

    def refresh(self, proxy_id=None):
        proxy_id = __find_proxy_id(proxy_id)
        j = self.__refresh(proxy_id)
        return j["success"]

    def list_proxies(self):
        r = self.__list()
        return r["proxies"]

    def requests_config(self, proxy_id=None):
        proxy_id, r = self.__find_proxy_id(proxy_id)
        proxy = [ p for p in r["proxies"] if p["id"] == proxy_id ][0]
        http_url = proxy["http"]
        http_url = http_url.replace("http://", "")
        return {
            "http": f"http://{proxy['username']}:{proxy['password']}@{http_url}",
            "https": f"http://{proxy['username']}:{proxy['password']}@{http_url}"
        }
        
    def __list(self):
        r = requests.get(f"{PP_API_SERVER}/list", headers=self.__headers)
        if r.status_code == 200:
            return r.json()
        elif r.status_code == 401:
            raise BadCredentialsException("Invalid token")
        else:
            raise NetworkException("Network Error")
    
    def __refresh(self, proxy_id):
        j = {
            'id': proxy_id
        }

        r = requests.post(f"{PP_API_SERVER}/refresh", headers=self.__headers, json=j)

        if r.status_code == 200:
            return r.json()
        elif r.status_code == 401:
            raise BadCredentialsException("Invalid token")
        elif r.status_code == 429:
            raise TooManyRefreshesException("Too many refreshes, please wait some time or contact support for increased limits")
        else:
            raise NetworkException("Network Error")