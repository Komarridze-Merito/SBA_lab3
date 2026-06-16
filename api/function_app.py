import azure.functions as func
import logging
from random import choice
import string
import json

# SYMBOLS = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="lab3")
def lab3(req: func.HttpRequest) -> func.HttpResponse:
    try:
        req_body = req.get_json()
        length = req_body.get('length')


        key = ''.join(choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(length))


        return func.HttpResponse(
            json.dumps({"key": key}),
            mimetype="application/json"
        )


    except Exception as e:
        return func.HttpResponse(
            f"Error processing request: {str(e)}",
            status_code=400
        )