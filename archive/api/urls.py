from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
  #url('^$', views.compare_price, name='compare_price'),
  url('^$', views.test, name='compare_price'),
  #url('^compare_price', views.compare_price, name='compare_price'),
)
