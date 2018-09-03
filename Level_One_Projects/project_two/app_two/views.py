from django.shortcuts import render
from django.http import HttpResponse
from app_two.models import User

def index(request):
    return render(request, 'app_two/index.html')

def users(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'users':user_list}
    return render(request, 'app_two/users.html', context=user_dict)

def help(request):
    help_dict = {'help_insert':"Help page."}
    return render(request, 'app_two/help.html', context=help_dict)
