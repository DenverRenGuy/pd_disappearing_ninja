from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^ninjas/(?P<color>[^/]+)', views.ninjas),
    url(r'^ninjas', views.all),

]
