# Simple rest service

This service can perform filtering and sorting operations on the given dataset.
## How to try
```
flask run
```
After that you can perform simple GET requests to the http://localhost:5000/compensation_data endpoint. For example:
```
GET /compensation_data?bonus=0&fields=primary_country,gender,salary&sort=salary
```
The response for this will be in similar format:
```
{"result": "ok", "data": [{"primary_country": "Romania (RO)", "gender": "Male", "salary": 2500.0}, ...
```
## Fields
- timestamp
- employment_type
- company_name
- company_size
- primary_country
- primary_city
- company_industry
- company_pub
- experience_overall
- experience_company
- job_title
- job_ladder
- job_level
- hours_per_week_req
- hours_per_week_act
- education
- salary
- bonus
- stock_options
- insurance
- vacation
- position_happiness
- plan_to_resign
- industry_direction_thoughts
- gender
- top_skills
- bootcamp_thoughts

## Possible operations
- Filter by column value: ?column_name1=value1&column_name2=value2&...
- Sort by columns: ?sort=column_name1,column_name2, ...
- Specify fields: ?fields=column_name1,column_name2, ...
- You can also apply condition to the field names:
  - column[gte]=value - Greater or equal
  - column[gt]=value - Greater than the value
  - column[le]=value - Lower or equal
  - column[l]=value - Lower than the value
  - column[e]=value - Equal to the value

## Run unit tests
```
python -m unittest -v unit_tests
```