from flask.blueprints import Blueprint

from api.utils.custom_response import SUCCESS_CODE, custom_response


health_api = Blueprint('health_api', __name__)


@health_api.route('/liveness', methods=['GET'])
def liveness():
    return custom_response({'status': 'OK'}, SUCCESS_CODE)