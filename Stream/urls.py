from django.conf.urls import url
from Stream import views

urlpatterns = [
    url(r'^$', views.post_list),
]
