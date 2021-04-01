from django.shortcuts import render
from django.http import HttpResponse
import requests
import json

def home(request):
	return render(request,'home.html')

def result(request):
	code=request.GET['code']
	state=request.GET['state']

	url='https://oauth2.googleapis.com/token'
	data = {'grant_type':'authorization_code',
			'code':code,
            'redirect_uri':'http://127.0.0.1:8000/result',
            'client_id':'client id',
            'client_secret':'client secret'
            }
	r=requests.post(url,data=data)
	token=r.json()['access_token']
	id_token=r.json()['id_token']
	url='https://oauth2.googleapis.com/tokeninfo?id_token='+id_token
	# headers = {"Authorization": "Bearer "+token}
	r = requests.get(url)
	print(r.json())
	return HttpResponse(r)