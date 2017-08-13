from django.conf.urls import url
import view
import di
import settings
from django.conf.urls.static import static

urlpatterns = [
	url(r'^login/', view.login),
	url(r'^index/', view.index),
	url(r'^pi/', view.person_info),
	url(r'^um/', view.user_manage),
	url(r'^sr/', view.score_rank),
	url(r'^api/create_new/', view.createnew),
	url(r'^api/delete_user/', view.deleteuser),
	url(r'^api/reset_pass/', view.resetpass),
	url(r'^api/get_profile/', view.getprofile),
	url(r'^api/update_profile/', view.updateprofile),
	url(r'^api/add_score/', view.add_score),
	url(r'^api/stu_scores/', view.stu_scores),
	url(r'^api/stu_rank/', view.stu_rank),
	url(r'^api/new_pass/', view.new_pass),
	url(r'^api/new_fb/', view.new_fb),
	url(r'^di/api/get_task/', di.get_task),
	url(r'^di/api/add_task/', di.add_task),
    url(r'', view.tologin),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)