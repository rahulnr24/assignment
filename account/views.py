from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from .forms import LoginForm
from django.contrib import messages

# Create your views here.
def login_view(request):

    form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                messages.success(request, "login successfully")
                return redirect("home")
            else :
                 messages.error(request, "username or password is incorrect")


    context={ 'form' : form }
    return render(request, 'account/login.html', context)