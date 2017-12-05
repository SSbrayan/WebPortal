from django.conf.urls import url

from . import views


app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

    url(r'^targets/$', views.TargetIndexView.as_view(), name='targetindex'),
    url(r'^targets/(?P<pk>[0-9]+)/$', views.TargetDetailView.as_view(), name='targetdetail'),
    url(r'^targets/(?P<target_id>[0-9]+)/update_IP$', views.update_IP, name='update_IP'),
    url(r'^targets/(?P<target_id>[0-9]+)/get_port_status$', views.info_update, name='info_update'),
]
