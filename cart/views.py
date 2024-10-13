from django.shortcuts import render
from .models import user_collection
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("<h1>This is running ..... Talib ...Mir </h1>")

def add_person(request):
    records={
        "firstname":"Talib",
        "lastname":"Mir"
    }
    user_collection.insert_one(records)
    return HttpResponse("New Person is added")
def all_person(request):
     x=user_collection.find()
     return(x)
