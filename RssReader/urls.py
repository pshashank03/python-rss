from django.conf.urls import *
from RssReader.views import *

urlpatterns = [
   url(r'home/^$', home),
]