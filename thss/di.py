from api import api_get_task, api_add_task
from django.http import HttpResponse
import json

def get_task(request):
	if request.method == 'GET':
		year = request.GET['year']
		month = request.GET['month']
		tasks = api_get_task(year, month)
		return HttpResponse(json.dumps({'status': 1, 'tasks': tasks}), content_type="application/json") 
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 

def add_task(request):
	if request.method == 'GET':
		year = request.GET['year']
		month = request.GET['month']
		day = request.GET['day']
		user = request.GET['user']
		content = request.GET['content']
		if api_add_task(year, month, day, user, content):
			return HttpResponse(json.dumps({'status': 1}), content_type="application/json") 
		else:
			return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 