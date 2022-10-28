from flask import Blueprint
import redis
from api.utils.constants import MONGODB_TESTS_COLLECTION, REDIS_TEST_DB
from api.utils.custom_response import SUCCESS_CODE, custom_response
from api.utils.mongo_adapter_factory import create_database_connection
from api.utils.queue_factory import create_queue_connection

test_api = Blueprint('test_api', __name__)

redis = create_queue_connection(REDIS_TEST_DB)
mongo = create_database_connection(MONGODB_TESTS_COLLECTION)

@test_api.route('/<test_id>', methods=['GET', 'POST'])
def exec_test(test_id):
    redis.lpush('test', test_id)
    return custom_response({'status': f'Test {test_id} inserted on the queue.'}, SUCCESS_CODE)

@test_api.route('/report/<test_id>', methods=['GET'])
def test_report(test_id):
    cursor = mongo.find({'test_id': int(test_id)})
    report = []
    for item in cursor:
        report.append({**item, '_id': str(item['_id'])})
    return custom_response({'report': report}, SUCCESS_CODE)