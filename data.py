import pandas

raw_data = pandas.read_csv("data/salary_survey.csv")
column_names = set(raw_data.columns)
possible_operations = {'fields', 'sort'}