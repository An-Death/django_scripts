from django.conf.urls import url

from . import views

app_name='param_table_for_customer'
urlpatterns = [
    # url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^(?P<server_id>[0-9]+)/*$', views.wells, name='wells'),
    url(r'^/table_(?P<well_id>[0-9]+)/$', views.table, name='table')
    # #  ex: /poll/5/
    # url(r'^(?P<question_id>[0-9]+)/*$', views.Test.detail, name='detail'),
    # #  ex /poll/5/results
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.Test.results, name='results'),
    # # ex /poll/123123/vote
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.Test.vote, name='vote')

]