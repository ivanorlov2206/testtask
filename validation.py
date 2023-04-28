import data


def validate_fields_for_operation(operation, fields_s):
    if fields_s is None:
        return False, "Fields value is empty for {}".format(operation)
    fields = fields_s.split(',')
    for field in fields:
        if field not in data.column_names:
            return False, "Wrong field '{}' for '{}'".format(field, operation)
    return True, ""


def preprocess_argument(val):
    if val.rstrip() == "":
        return None
    if val.isnumeric():
        return float(val)
    return val
