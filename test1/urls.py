from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^111/$',views.rendermy)
]