"""
Caching is a powerful tool. In this case we improved our application’s performance by limiting the number of external HTTP requests. We cut out the latency from the actual HTTP request itself.
In many cases, you are not just making a request. You have to process the request as well, which could involve hitting a database, performing some sort of filtering, etc. Thus, caching can cut the latency from the processing of the request as well.
Again, in the above example, we expire the cache (commonly known as flushing) after 180 seconds in order to deliver the most up-to-date data to the end user. Think about that for a minute.
Is it really necessary to flush it that regularly? Probably not. In this application, we could get away with changing this to five or ten minutes since it’s not a huge issue if we miss a few new users added to the API every now and then.
That said, you really want to pay close attention to flushing when the data is time-sensitive and paramount to your application’s core functionality.
For example, if you were pulling data from an API that is updated several times a minute (like a seismic activity API) and your end user must have the most updated data, then you would want to expire it every 30 or 60 seconds or so.
It’s also important to balance the flushing frequency vs. the amount of time the call takes. If your API call is fairly expensive - perhaps it takes one to five seconds - then you want to increase the amount of time between flushing to improve performance.
"""
# https://diveintopython3.net/http-web-services.html
# EPAM
from datetime import datetime, timedelta

class Cache:
    cache = None
    default_time = None
    
    def __init__(self, default_time=3):
        self.cache = {}
        self.default_time = timedelta(seconds=default_time)
    
    def hash_key(self, val):
        return hash(val)
    
    def add(self, key, val, timeout=None):
        expire = datetime.now() + (timedelta(seconds=timeout) if timeout else self.default_time)
        self.cache[self.hash_key(key)] = expire, val
        
    def get(self, key):
        key = self.hash_key(key)
        if key in self.cache:
            if datetime.now() < self.cache[key][0]:
                return self.cache[key][1]
            else:
                self.cache.pop(key)
        return None

url_cache = Cache(60)

# class Cache:
#     cache = None

#     def __init__(self):
#         self.cache = {}

#     def add(self, key, val, timeout=None):
#         self.cache[key] = val
        
#     def get(self, key):
#         if key in self.cache:
#             return self.cache[key][1]
#         return None

# url_cache = Cache()