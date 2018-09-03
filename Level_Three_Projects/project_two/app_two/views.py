from django.shortcuts import render
from app_two.forms import NewUserForm

def index(request):
    return render(request, 'app_two/index.html')

def users(request):

    form = NewUserForm()

    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print('ERROR FORM INVALID')

    return render(request, 'app_two/users.html', {'form':form})
