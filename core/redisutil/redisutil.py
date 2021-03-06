import redis
import os

redis_pool = None

def init():
    global redis_pool
    print("PID %d: initializing redis pool..." % os.getpid())
    redis_pool = redis.ConnectionPool(host='192.168.30.195', port=6379)

def getRedisConn():
    return redis.Redis(connection_pool=redis_pool)

