from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from settings import FIREBASE_APP
from .serializers import *
import requests, threading, json

def long_process():
    print(FIREBASE_APP)
    db = FIREBASE_APP.database()
    db.child('danger').set(True)
    print(FIREBASE_APP)

def init_subproccess():
    t = threading.Thread(target=long_process, args={}, kwargs={})
    t.setDaemon(True)
    t.start()

def call_ws():
    URL = 'http://localhost:3000/publish'
    payload = {'some': 'data'}
    r = requests.post(URL, json=payload)
    print(r)
    

def index(request):
    call_ws()
    #init_subproccess()
    return HttpResponse('A')