import json
from flask import Flask, make_response, request, jsonify
from app.db.backend import numbers_to_add
from app.helper.utils import sum_list


app = Flask(__name__)


@app.route("/total")
def total():
    """
    Returns the sum of a list
    
    """
    data = int(sum_list(numbers_to_add))
    result = {"total": data}
    return make_response(json.dumps(result), 200)

