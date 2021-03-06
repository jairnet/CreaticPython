from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

from django.views.generic import ListView, DetailView

from apps.usuarios.models import Perfil
from apps.home.mixins import DashboardLoginRequiredMixin

# Exections
from django.db.utils import IntegrityError


# class UserDetailView(DashboardLoginRequiredMixin, DetailView):
#     model = User
#     template_name = 'usuarios/user_detail.html'

#     def get_success_url(self):
#         return reverse("dashboard")


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'usuarios/login.html', {'error':'Usuario o Password incorrectos'})
    return render(request, 'usuarios/login.html')


def logoutView(request):
    logout(request)
    return redirect('login')

def signupView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        
        if password != password_confirmation:
            return render(request, 'usuarios/signup.html', {'error':'Password no coinciden'})
        try: 
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            return render(request, 'usuarios/signup.html', {'error':'Usuario ya existe'})
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        perfil = Perfil(usuraio=user)
        perfil.save()

        return redirect('login')

    return render(request, 'usuarios/signup.html')