from django.conf.urls import url
from app_two import views

urlpatterns = [
    url(r'^users/', views.users, name='users'),
]
