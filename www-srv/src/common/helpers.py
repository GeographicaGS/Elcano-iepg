# coding=UTF8

"""

Common helpers.

"""
import hashlib
import memcache
from config import MemcachedConfig

def cacheWrapper(funcName, *args, **kwargs):
    """Cache wrapping helper."""
    if MemcachedConfig["enabled"]:
        h = hashlib.sha256(funcName.__name__+str(args)+str(kwargs)).hexdigest()
        mc = memcache.Client([MemcachedConfig["host"]+":"+MemcachedConfig["port"]], debug=0)
        v = mc.get(h)
        if v:
            return(v)
        else:
            out = funcName(*args, **kwargs)
            mc.set(h, out, MemcachedConfig["expiration"])
            return(out)
    else:
        return(funcName(*args, **kwargs))
