from django.shortcuts import render
from app.models import *
from django.http import HttpResponse
# Create your views here.

def insert_Coutry(request):
    c=input('enter coutry name')
    p=input('enter population')
    CO=Country.objects.get_or_create(cname=c,cpopulation=p)[0]
    CO.save()
    return HttpResponse ('Coutry data is inserted ')


def insert_Capital(request):
    c=input('enter coutry name')
    CO=Country.objects.get_or_create(cname=c)[0]
    CO.save()
    cn=input('enter capital name')
    cp=input('enter a capital population')
    PO=Capital.objects.get_or_create(cname=CO,capital_name=cn,capital_population=cp)[0]
    PO.save()
    return HttpResponse ('capital data is inserted')

