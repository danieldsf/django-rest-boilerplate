from django.shortcuts import render
from django.utils.safestring import mark_safe
from django.http import HttpResponse
import requests as req 

# Def Send POST:

def call_websocket():
    payload = {'some': 'data'}
    r = req.post('http://localhost:3000/publish', json=payload)
    print(r)

def index(request):
    call_websocket()
    return HttpResponse('A')