import json

from flask import Flask, request
import app.data as data
from app.data_processing import is_column, parse_column_and_modifier, filter_by_column_value, is_operation, \
    perform_sort, limit_fields, replace_nan_with_null
from app.validation import preprocess_argument, validate_fields_for_operation

app = Flask(__name__)


def make_error(message):
    return json.dumps({"result": "error", "reason": message})


@app.route('/compensation_data')
def comp_data():
    args = request.args.to_dict()
    data_to_return = data.raw_data

    # Validate all parameters
    for param, value in args.items():
        value = preprocess_argument(value)
        if is_column(param):
            column_name, modifier = parse_column_and_modifier(param)
            if not column_name:
                return make_error("Bad field name: {}".format(param))
            data_to_return = filter_by_column_value(data_to_return, column_name, modifier, value)
        elif is_operation(param):
            is_success, msg = validate_fields_for_operation(param, value)
            if not is_success:
                return make_error(msg)
        else:
            return make_error("Wrong field: {}".format(param))

    if 'sort' in args:
        data_to_return = perform_sort(data_to_return, args['sort'].split(','))

    if 'fields' in args:
        data_to_return = limit_fields(data_to_return, args['fields'].split(','))

    data_to_return = replace_nan_with_null(data_to_return)
    return json.dumps({"result": "ok", "data": data_to_return.to_dict(orient='records')})
