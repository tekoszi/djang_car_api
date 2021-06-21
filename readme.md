# This is a CAR REST API
This api enables you CRUD cars<br>
I have build a postman collection which enables you to verify all the queries, it is available here: https://www.getpostman.com/collections/8cea83931a1e4cf26a02

### Avaiable Endpoints:<br>
# /car<br>
Enables to add new car as long as it is correct based on https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json
#### Available queries:<br>
POST with body:
```json
 {
    "make": "honda",
    "model": "Accord"
}
```
example response:
```json
{
'Car was added to the database'
}
```
# /cars<br>
#### Available queries:<br>
GET <br>
Enables to query for all of the cars in the DB
example response:
```json
{
    "car_list": [
        {
            "id": 1,
            "make": "honda",
            "model": "Accord",
            "avg_rating": 5.0
        },
        {
            "id": 2,
            "make": "honda",
            "model": "Accord",
            "avg_rating": 0
        },
        {
            "id": 3,
            "make": "honda",
            "model": "Accord",
            "avg_rating": 0
        },
        {
            "id": 4,
            "make": "honda",
            "model": "Accord",
            "avg_rating": 0
        },
        {
            "id": 5,
            "make": "honda",
            "model": "Accord",
            "avg_rating": 0
        },
        {
            "id": 6,
            "make": "honda",
            "model": "Accord",
            "avg_rating": 5.0
        },
        {
            "id": 8,
            "make": "honda",
            "model": "Accord",
            "avg_rating": 0
        }
    ]
}
```
#
DELETE<br>
Enables to remove car based on its ID<br>
exaple query: http://127.0.0.1:8000/cars/{ id } <br>
example responses:
```json
{
    'Car id not found''
}
```
```json
{
    'Car no. 4 was removed'
}
```
#
# /rate<br>
Enables to rate car based on its id
#### Available queries:<br>
POST with body:
```json
{
"car_id": 9,
"rating": 5
}
```

example responses: <br>
```json
{
    'There is no car with that id''
}
```
```json
{
    'Car was rated''
}
```
```json
{
    'Only 1-5 rating allowed''
}
```

#
# /popular<br>
Enables to query for top 5 car based on number of rates
#### Available queries:<br>
GET

example responses: <br>
```json
{
    "top_cars": [
        {
            "carId": 1,
            "make": "honda",
            "model": "Accord",
            "rates_number": 10
        },
        {
            "carId": 6,
            "make": "honda",
            "model": "Accord",
            "rates_number": 5
        },
        {
            "carId": 2,
            "make": "honda",
            "model": "Accord",
            "rates_number": 0
        },
        {
            "carId": 3,
            "make": "honda",
            "model": "Accord",
            "rates_number": 0
        },
        {
            "carId": 5,
            "make": "honda",
            "model": "Accord",
            "rates_number": 0
        }
    ]
}
```
#
# You can create and run docker container for this application by running docker-compose up
# You can create and run docker container for this application by running docker-compose up
