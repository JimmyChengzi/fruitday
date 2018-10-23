from django.conf.urls import url
from userinfo.views import *

urlpatterns = [
    url(r'^registerin/',register_,name='registerin'),
]
