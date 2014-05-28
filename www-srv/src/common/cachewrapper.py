# coding=UTF8

"""

Cache wrapper.

"""
import common.config as config

def cacheWrapper(funcName, *args, **kwargs):
    """Cache wrapping helper."""
    if config.MemcachedConfig["enabled"]:
        s = ""
        for i in args:
            s+=str(i)
        for i in kwargs:
            s+=str(i)
        h = hashlib.sha256(funcName.__name__+s).hexdigest()
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


