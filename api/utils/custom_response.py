from flask import json, Response

SUCCESS_CODE = 200
ERROR_CODE = 500


def custom_response(res, status_code):
    return Response(
        mimetype='application/json',
        response=json.dumps(res),
        status=status_code
    )