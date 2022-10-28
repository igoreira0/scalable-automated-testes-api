from flask import Blueprint
import redis
import pymongo
from api.utils.constants import MONGO_URI, MONGODB_DATABASE, MONGODB_TESTS_COLLECTION, REDIS_HOST, REDIS_PASS, REDIS_PORT, REDIS_TEST_DB, REDIS_USER
from api.utils.custom_response import SUCCESS_CODE, custom_response

test_api = Blueprint('test_api', __name__)

mongo = pymongo.MongoClient(MONGO_URI)[MONGODB_DATABASE][MONGODB_TESTS_COLLECTION]

@test_api.route('/<test_id>', methods=['GET', 'POST'])
def exec_test(test_id):
    with redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=REDIS_TEST_DB, ssl=True, username=REDIS_USER, password=REDIS_PASS) as redis_client:
        redis_client.lpush('test', test_id)
    return custom_response({'status': f'Test {test_id} inserted on the queue.'}, SUCCESS_CODE)

@test_api.route('/report/<test_id>', methods=['GET'])
def test_report(test_id):
    cursor = mongo.find({'test_id': int(test_id)})
    report = []
    for item in cursor:
        report.append({**item, '_id': str(item['_id'])})
    return custom_response({'report': report}, SUCCESS_CODE)