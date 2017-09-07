from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /poll/
    url(r'^$', views.index, name='index'),
    #  ex: /poll/5/
    url(r'^(?P<question_id>[0-9]+)/*$', views.detail, name='detail'),
    #  ex /poll/5/results
    url(r'^(?P<question_id>[0-9]+)/result(s*)/$', views.results, name='results'),
    # ex /poll/123123/vote
    url(r'^(?P<question_id>[0-9]+)/vote(s*)/$', views.vote, name='vote')

]
