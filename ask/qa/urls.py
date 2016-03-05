from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login/', views.test),
    url(r'^signup/', views.test),
    url(r'^question/(?P<id>[^/]+)', views.one_quest),
    url(r'^ask/', views.test),
    url(r'^popular/', views.popular_quests),
    url(r'^new/', views.test),
]