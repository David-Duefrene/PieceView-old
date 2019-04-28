from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import LoginForm

# The Login button itself
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): # Are fields are filled in?
            cd = form.cleaned_data
            user = authenticate(request, # check user/pw
                                username=cd['username'],
                                password=cd['password'])
            if user is not None: # If user is valid
                if user.is_active:
                    login(request, user) # logs the session in
                    return HttpResponse('Authenticated '\
                                        'successfully')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})

# Renders the dashboard if the user is logged in
@login_required
def dashboard(request):
    return render(request,
                  'account/dashboard.html',
                  {'section': 'dashboard'})