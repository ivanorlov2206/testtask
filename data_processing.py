import numpy as np
import re


def limit_fields(dt, fields):
    return dt[fields]


def perform_sort(dt, fields):
    return dt.sort_values(by=fields)


def parse_column_and_modificator(arg):
    operation_re = r'\[(gte|le|gt|l|e)\]$'
    match = re.search(operation_re, arg)
    if match:
        op = match.group()
        return arg.split('[')[0], op
    if '[' in arg:
        return None, None
    return arg, ""


def filter_by_column_value(dt, col, op, value):
    if op == '[gte]':
        return dt.loc[dt[col] >= value]
    elif op == '[le]':
        return dt.loc[dt[col] <= value]
    elif op == '[gt]':
        return dt.loc[dt[col] > value]
    elif op == '[l]':
        return dt.loc[dt[col] < value]
    else:
        return dt.loc[dt[col] == value]


def replace_nan_with_null(dt):
    return dt.replace({np.nan: None})
