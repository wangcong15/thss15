from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from api import check_cookie, check_login, user_list, new_user, delete_user, get_profile, update_profile, update_a_profile, new_scores, get_scores, get_rank, update_pass, get_a_rank, add_feed_back, reset_pass
import md5
import json
from django.views.decorators.csrf import csrf_exempt

def tologin(request):
    return HttpResponseRedirect('/login/')

def index(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponseRedirect('/login/')
	username = request.COOKIES['qwer']
	if rank == 0:
		return render_to_response('superadmin.html', {'user_name': username}, context_instance=RequestContext(request))
	elif rank == 1:
		return render_to_response('admin.html', {'user_name': username}, context_instance=RequestContext(request))
	else:
		return render_to_response('ordinaryuser.html', {'user_name': username}, context_instance=RequestContext(request))

def login(request):
	(flag, rank) = check_cookie(request)
	if flag:
		return HttpResponseRedirect('/index/')
	if request.method == 'GET':
		return render_to_response('login.html', {}, context_instance=RequestContext(request))
	elif request.method == 'POST':
		username = request.POST['form-username']
		password = request.POST['form-password']
		m1 = md5.new()
		m1.update(password)
		password = m1.hexdigest()
		if(check_login(username, password)):
			response = HttpResponseRedirect('/index/')
			response.set_cookie('qwer', username, 3600)
			response.set_cookie('asdf', password, 3600)
			return response
		else:
			return render_to_response('login.html', {'errro_message':"Wrong Username Or Password"}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

def person_info(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponseRedirect('/login/')
	if rank == 0:
		username = request.COOKIES['qwer']
		return render_to_response('personalinfo.html', {'user_name': username}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

def user_manage(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponseRedirect('/login/')
	if rank == 0:
		username = request.COOKIES['qwer']
		(userlist, countdic) = user_list()
		total = countdic['0'] + countdic['1'] + countdic['2']
		return render_to_response('usermanage.html', {'user_name': username, 'userlist': userlist, 'countdic': countdic, 'total': total}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

def score_rank(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponseRedirect('/login/')
	if rank == 2:
		username = request.COOKIES['qwer']
		result_scores = get_scores(username)
		return render_to_response('scorerank.html', {'user_name': username, 'scores': result_scores}, context_instance=RequestContext(request))
	else:
		return HttpResponseRedirect('/login/')

@csrf_exempt
def createnew(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	if rank == 0 and request.method == 'POST':
		username = request.POST['new_username']
		rank = request.POST['new_rank']
		password = username
		m1 = md5.new()
		m1.update(password)
		password = m1.hexdigest()
		if new_user(username, password, rank):
			return HttpResponse(json.dumps({'status': 1}), content_type="application/json") 
		else:
			return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 

@csrf_exempt
def deleteuser(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	if rank == 0 and request.method == 'POST':
		username = request.POST['username']
		if delete_user(username):
			return HttpResponse(json.dumps({'status': 1}), content_type="application/json") 
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 

@csrf_exempt
def resetpass(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	if rank == 0 and request.method == 'POST':
		username = request.POST['username']
		password = username
		m1 = md5.new()
		m1.update(password)
		password = m1.hexdigest()
		if reset_pass(username, password):
			return HttpResponse(json.dumps({'status': 1}), content_type="application/json") 
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 

def getprofile(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	if rank == 0 and request.method == 'GET':
		username = request.GET['username']
		profile = get_profile(username)
		return HttpResponse(json.dumps({'status': 1, 'profile': profile}), content_type="application/json") 
	elif rank == 2 and request.method == 'GET':
		username = request.COOKIES['qwer']
		profile = get_profile(username)
		return HttpResponse(json.dumps({'status': 1, 'profile': profile}), content_type="application/json") 
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 

@csrf_exempt
def updateprofile(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	if rank == 0 and request.method == 'POST':
		mstuid = request.POST['stuid']
		mclass = request.POST['class']
		mtel = request.POST['tel']
		memail = request.POST['email']
		username = request.POST['current_user']
		if update_profile(username, mstuid, mclass, mtel, memail):
			return HttpResponse(json.dumps({'status': 1}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({'status': 0}), content_type="application/json")
	elif rank == 2 and request.method == 'POST':
		mtel = request.POST['new_telep']
		memail = request.POST['new_email']
		username = request.COOKIES['qwer']
		if update_a_profile(username, mtel, memail):
			return HttpResponse(json.dumps({'status': 1}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({'status': 0}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 

@csrf_exempt
def add_score(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	if rank == 0 and request.method == 'POST':
		stuid = request.POST.getlist('stuid[]')
		cname = request.POST.getlist('cname[]')
		scores = request.POST.getlist('score[]')
		weigh = request.POST.getlist('weigh[]')
		style = request.POST.getlist('style[]')
		terms = request.POST.getlist('terms[]')
		if new_scores(stuid, cname, scores, weigh, style, terms):
			return HttpResponse(json.dumps({'status': 1}), content_type="application/json")
		else:
			return HttpResponse(json.dumps({'status': 0}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 

def stu_scores(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	if rank == 0 and request.method == 'GET':
		stuname = request.GET['stuname']
		scores = get_scores(stuname)
		return HttpResponse(json.dumps({'status': 1, 'scores': scores}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 

def stu_rank(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	if rank == 0 and request.method == 'GET':
		flag = request.GET['flag']
		ranks = get_rank(flag)
		return HttpResponse(json.dumps({'status': 1, 'rank': ranks}), content_type="application/json")
	elif rank == 2 and request.method == 'GET':
		flag = request.GET['flag']
		username = request.COOKIES['qwer']
		ranks = get_a_rank(username, flag)
		return HttpResponse(json.dumps({'status': 1, 'rank': ranks}), content_type="application/json")
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 

@csrf_exempt
def new_pass(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	if rank == 2 and request.method == 'POST':
		new_password = request.POST['new_pass']
		username = request.COOKIES['qwer']
		m1 = md5.new()
		m1.update(new_password)
		new_password = m1.hexdigest()
		if update_pass(username, new_password):
			return HttpResponse(json.dumps({'status': 1, 'new_password': new_password}), content_type="application/json") 
		else:
			return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 

def new_fb(request):
	(flag, rank) = check_cookie(request)
	if not flag:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	if rank == 2 and request.method == 'GET':
		fb = request.GET['fb']
		if add_feed_back(fb):
			return HttpResponse(json.dumps({'status': 1}), content_type="application/json") 
		else:
			return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 
	else:
		return HttpResponse(json.dumps({'status': 0}), content_type="application/json") 