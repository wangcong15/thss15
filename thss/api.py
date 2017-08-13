from django.contrib.auth.hashers import make_password, check_password
from django.conf import settings
from models import users, profile, score, feedback, tasks

def check_cookie(request):
    d = request.COOKIES.keys()
    if "qwer" in d and "asdf" in d:
        username = request.COOKIES['qwer']
        password = request.COOKIES['asdf']
        select_user = users.objects.filter(uname=username).filter(upass=password)
        if len(select_user) == 0:
            return (False, -1)
        else:
        	return (True,  select_user[0].urank)
    else:
        return (False, -1)

def check_login(username, password):
	select_user = users.objects.filter(uname=username).filter(upass=password)
	if len(select_user) == 0:
		return False
	else:
		return True

def user_list():
    user_list = users.objects.all()
    result = []
    count_dic = {'0':0, '1':0, '2':0}
    for user in user_list:
        count_dic[str(user.urank)] += 1
        result.append({'username': user.uname, 'rank':user.urank})
    return (result, count_dic)

def new_user(username, password, rank):
    select_user = users.objects.filter(uname=username)
    if len(select_user) != 0:
        return False
    else:
        a_new_user = users(uname=username, upass=password, urank=rank)
        a_new_user.save()
        return True

def delete_user(username):
    users.objects.get(uname=username).delete()
    return True

def reset_pass(username, password):
    users.objects.filter(uname=username).update(upass=password)
    return True

def get_profile(username):
    a_user = users.objects.filter(uname=username)
    if len(a_user) != 1:
        return {}
    else:
        a_user = a_user[0]
        a_profile = profile.objects.filter(puser=a_user)
        if len(a_profile) != 1:
            return {}
        a_profile = a_profile[0]
        result = {'stuid': a_profile.pstuid, 'class': a_profile.pclass, 'tel': a_profile.ptel, 'email': a_profile.pemail}
        return result

def update_profile(username, mstuid, mclass, mtel, memail):
    a_user = users.objects.filter(uname=username)
    if len(a_user) != 1:
        return False
    else:
        a_user = a_user[0]
        a_profile = profile.objects.filter(puser=a_user)
        if len(a_profile) == 0:
            mclass = int(mclass)
            new_profile = profile(pstuid=mstuid, pclass=mclass, ptel=mtel, pemail=memail, puser=a_user)
            new_profile.save()
            return True
        elif len(a_profile) == 1:
            mclass = int(mclass)
            a_profile.update(pstuid=mstuid, pclass=mclass, ptel=mtel, pemail=memail)
            return True
        else:
            return False

def update_a_profile(username, mtel, memail):
    a_user = users.objects.filter(uname=username)
    if len(a_user) != 1:
        return False
    else:
        a_user = a_user[0]
        a_profile = profile.objects.filter(puser=a_user)
        if len(a_profile) != 1:
            return False
        else:
            a_profile.update(ptel=mtel, pemail=memail)
            return True

def new_scores(stuid, cname, scores, weigh, style, terms):
    for i in range(0, len(stuid)):
        curr_stuid = stuid[i]
        curr_cname = cname[i]
        curr_score = scores[i]
        curr_weigh = weigh[i]
        curr_style = style[i]
        curr_terms = terms[i]
        find_score = score.objects.filter(sstuid=curr_stuid).filter(scname=curr_cname).filter(sscore=curr_score).filter(sweigh=curr_weigh).filter(sstyle=curr_style).filter(sterms=curr_terms)
        if len(find_score) != 0:
            continue
        else:
            a_score = score(sstuid=curr_stuid, scname=curr_cname, sscore=curr_score, sweigh=curr_weigh, sstyle=curr_style, sterms=curr_terms)
            a_score.save()
    return True

def get_scores(stuname):
    a_user = users.objects.filter(uname=stuname)
    if len(a_user) != 1:
        return []
    else:
        a_user = a_user[0]
        a_profile = profile.objects.filter(puser=a_user)
        if len(a_profile) == 0:
            return []
        else:
            a_profile = a_profile[0]
            stuId = a_profile.pstuid
            scores = score.objects.filter(sstuid=stuId)
            result = []
            for a_score in scores:
                result.append({'StuId': a_score.sstuid, 'StuName': a_user.uname, 'CourseName': a_score.scname, 'Score': a_score.sscore, 'Weigh': a_score.sweigh, 'Style': a_score.sstyle})
            return result

def get_rank(flag):
    result = []
    score_dic = {}
    if flag == "0" or flag == "1":
        all_scores = score.objects.all()
    else:
        all_scores = score.objects.filter(sterms__gt=20160900)
    for a_score in all_scores:
        stuid = a_score.sstuid
        mscore = a_score.sscore
        weigh = a_score.sweigh
        if score_dic.has_key(stuid):
            exist_item = score_dic[stuid]
            exist_item["totalWeigh"] += weigh
            exist_item["totalScore"] += weigh * mscore;
            if mscore == 0:
                exist_item["failCount"] += 1
        else:
            new_item = {"totalWeigh": weigh, "totalScore": weigh * mscore, "failCount": 0}
            score_dic[stuid] = new_item
    all_stu = profile.objects.all()
    for a_stu in all_stu:
        if score_dic.has_key(a_stu.pstuid):
            exist_rank = score_dic[a_stu.pstuid]
            new_rank = {'stuName': a_stu.puser.uname, 'averScore':exist_rank["totalScore"] / exist_rank["totalWeigh"], 'rank':0, 'failNum':exist_rank["failCount"], 'totalWeigh': exist_rank["totalWeigh"]}
            result.append(new_rank)
    result.sort(lambda x,y : cmp(y['averScore'], x['averScore']))
    rank_i = 1
    for a_result in result:
        a_result['rank'] = rank_i
        rank_i += 1
    return result

def get_a_rank(username, flag):
    result = []
    score_dic = {}
    if flag == "0" or flag == "1":
        all_scores = score.objects.all()
    else:
        all_scores = score.objects.filter(sterms__gt=20160900)
    for a_score in all_scores:
        stuid = a_score.sstuid
        mscore = a_score.sscore
        weigh = a_score.sweigh
        if score_dic.has_key(stuid):
            exist_item = score_dic[stuid]
            exist_item["totalWeigh"] += weigh
            exist_item["totalScore"] += weigh * mscore;
            if mscore == 0:
                exist_item["failCount"] += 1
        else:
            new_item = {"totalWeigh": weigh, "totalScore": weigh * mscore, "failCount": 0}
            score_dic[stuid] = new_item
    all_stu = profile.objects.all()
    a_stu_id_ave = -1
    for a_stu in all_stu:
        if score_dic.has_key(a_stu.pstuid):
            exist_rank = score_dic[a_stu.pstuid]
            new_rank = {'stuName': a_stu.puser.uname, 'averScore':exist_rank["totalScore"] / exist_rank["totalWeigh"], 'rank':0, 'failNum':exist_rank["failCount"], 'totalWeigh': exist_rank["totalWeigh"]}
            result.append(new_rank)
            if a_stu.puser.uname == username:
                a_stu_id_ave = exist_rank["totalScore"] / exist_rank["totalWeigh"]
                final_result = new_rank
    if a_stu_id_ave == -1:
        return []
    num_of_stu = len(result)
    final_rank = 1
    for a_result in result:
        if a_result['averScore'] > a_stu_id_ave:
            final_rank += 1
    final_result['rank'] = str(final_rank) + " / " + str(num_of_stu)
    fianl_arr = []
    fianl_arr.append(final_result)
    return fianl_arr

def update_pass(username, new_password):
    users.objects.filter(uname=username).update(upass=new_password)
    return True

def add_feed_back(fb):
    new_fb = feedback(fcontent=fb)
    new_fb.save()
    return True

def api_get_task(year, month):
    result = []
    mtask = tasks.objects.filter(tyear=year).filter(tmonth=month)
    for a_task in mtask:
        result.append({'user':a_task.tuser, 'date':a_task.tday, 'content':a_task.tcontent})
    return result

def api_add_task(year, month, day, user, content):
    new_task=tasks(tyear=year, tmonth=month, tday=day, tuser=user, tcontent=content)
    new_task.save()
    return True