from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import sqlite3

import json
import requests
from myapp.models import Car

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

@csrf_exempt
def post_car(request):
    if request.method == "POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)
        make = body["make"]
        model = body["model"]
        correctCarList = requests.get(f'https://vpic.nhtsa.dot.gov/api/vehicles/GetModelsForMake/{make}?format=json')
        makeModels = [x['Model_Name'] for x in correctCarList.json()['Results']]
        if model in makeModels:
            print('yes')
            newCar = Car(make=make,
                        model=model,
                        rates_number=0,
                        rates_total=0)
            newCar.save()
            return HttpResponse([{'Car was added to the database'}], content_type='text / json')
        else:
            return HttpResponse([{'Car was not added to the database'}], content_type='text / json')

@csrf_exempt
def get_cars(request):
    if request.method == "GET":
        queryset = Car.objects.all()
        result = []
        for obj in queryset:
            result.append({"id":obj.id, "make" : obj.make,  "model" : obj.model, "avg_rating" : obj.rates_total/obj.rates_number if obj.rates_number!=0 else 0})
        json_stuff = json.dumps({"car_list": result})
        if result:
            return HttpResponse(json_stuff, content_type='text/json')
        else:
            return HttpResponse([{'There are no cars in the database'}], content_type='text / json')

@csrf_exempt
def delete_car(request, car_id):
    if request.method == "DELETE":
        queryset = Car.objects.all()
        result = []
        for obj in queryset:
            result.append(obj.id)
        if car_id in result:
            Car.objects.filter(id=car_id).delete()
            return HttpResponse({f'Car no. {car_id} was removed'}, content_type='text/json')
        else:
            return HttpResponse({'Car id not found'}, content_type='text/json')

@csrf_exempt
def rate_car(request):
    if request.method == "POST":
        bodyunicode = request.body.decode('utf-8')
        body = json.loads(bodyunicode)
        car_id = body["car_id"]
        rating = body["rating"]
        queryset = Car.objects.filter(id=car_id)
        if queryset:
            if rating > 0 and rating <6:
                currentRatesTotal = Car.objects.filter(id=car_id)[0].rates_total
                Car.objects.filter(id=car_id).update(rates_total=currentRatesTotal+rating )

                currentRatesNumber = Car.objects.filter(id=car_id)[0].rates_number
                Car.objects.filter(id=car_id).update(rates_number=currentRatesNumber+ 1)
                return HttpResponse({'Car was rated'}, content_type='text/json')
            else:
                return HttpResponse({'Only 1-5 rating allowed'}, content_type='text/json')
        else:
            return HttpResponse({'There is no car with that id'}, content_type='text/json')

@csrf_exempt
def popular_car(request):
    if request.method == "GET":
        topCars = Car.objects.values('id', 'make', 'model', 'rates_number').order_by('-rates_number')[:5]
        json_stuff = json.dumps({"top_cars": [x for x in topCars]})
        if topCars:
            return HttpResponse({json_stuff}, content_type='text/json')
        else:
            return HttpResponse({'There are no cars in the DB'}, content_type='text/json')
