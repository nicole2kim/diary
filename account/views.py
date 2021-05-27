from django.core.exceptions import NON_FIELD_ERRORS
from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def first(request):
    return render(request, 'first.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request=request, username = username, password=password)
            if user is not None:
                login(request, user)
        return redirect("home")

    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect("first")

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
        return redirect('first')

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form})