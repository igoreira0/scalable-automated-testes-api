import redis

from api.utils.constants import REDIS_HOST, REDIS_PASS, REDIS_PORT, REDIS_TEST_DB, REDIS_USER



def create_queue_connection(DB):
    if not queue[REDIS_HOST][DB]:
        queue[REDIS_HOST][DB] = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_TEST_DB, ssl=True, username=REDIS_USER, password=REDIS_PASS)
    return queue[REDIS_HOST][DB]



queue = {
    REDIS_HOST: {
        REDIS_TEST_DB: None
    }
}