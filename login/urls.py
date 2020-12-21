from django.conf.urls import url
from login import views

urlpatterns = [
  url(r'^api/user$', views.user_list),
]