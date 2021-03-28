from redis import StrictRedis
import logging

# TODO use Key Vault
REDIS_KEY = 'PdO0tPKg6SEGLrLqrTbuOKljzy+z9knEjj9WEzMKobY='
REDIS_HOST = 'redis-cache-news-app.redis.cache.windows.net'
REDIS_PORT = 6380
REDIS_USE_SSL = True
REDIS_USE_ABORT_CONNECT = False
REDIS_LOGICAL_DB_INDEX = 0

def init_redis(redis = None):
    if redis:
        return redis
        
    logging.info('Init redis')

    assert(REDIS_LOGICAL_DB_INDEX >= 0)
    assert(REDIS_LOGICAL_DB_INDEX < 16)

    redis = StrictRedis(
        password=REDIS_KEY,
        host=REDIS_HOST,
        port=REDIS_PORT,
        ssl=REDIS_USE_SSL,
        db=REDIS_LOGICAL_DB_INDEX,
    )

    logging.info('Test redis with set(MessageSCRAP, ...)')
    result = redis.set("MessageSCRAP", "Hello!, The cache is working with Python!")
    logging.info("Test redis set(MessageSCRAP, ...) returned : " + str(result))

    return redis