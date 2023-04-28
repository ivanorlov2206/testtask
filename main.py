import json

import pandas
from flask import Flask, request

from data_processing import filter_by_column_value, replace_nan_with_null, limit_fields, perform_sort, \
    parse_column_and_modificator
from validation import validate_fields_for_operation, preprocess_argument

data = pandas.read_csv("data/salary_survey.csv")
app = Flask(__name__)
column_names = set(data.columns)

possible_operations = {'fields', 'sort'}


def make_error(message):
    return json.dumps({"result": "error", "reason": message})


@app.route('/compensation_data')
def comp_data():
    args = request.args.to_dict()
    data_to_return = data

    # Validate all parameters
    for param, value in args.items():
        value = preprocess_argument(value)
        column_name, modificator = parse_column_and_modificator(param)
        if not column_name:
            return make_error("Bad field name: {}".format(param))
        if column_name in column_names:
            data_to_return = filter_by_column_value(data_to_return, column_name, modificator, value)
        elif param in possible_operations:
            is_success, msg = validate_fields_for_operation(column_names, param, value)
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
