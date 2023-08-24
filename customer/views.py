from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Customer
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.


def user_register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        first_name = request.POST.get('name')
        last_name = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        new_user = User.objects.filter(username=username).first()

        if new_user:

            return HttpResponse(f'Usuário já cadastrado')
        
        else:
            new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username,email=email, password=password)
        
        new_user.save()

        return redirect(user_login)
        


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            
            return redirect(home)
        else:
            
            msg_error = 'Mensagem de erro.'
            messages.error(request, msg_error)
            return redirect(user_register)
        

def logout_view(request):
    logout(request)
    return redirect(user_login)

@login_required(login_url='/login/')
def home(request):

    customers = Customer.objects.all()
    return render(request, 'home.html', {'customers': customers})
        
def save(request):
    name = request.POST.get("name")
    cnpj = request.POST.get("cnpj")
    Customer.objects.create(name=name, cnpj=cnpj)
    customers = Customer.objects.all()
    return render(request, 'home.html', {'customers': customers})


def edit(request, id):
    customer = Customer.objects.get(id=id)
    return render(request, 'update.html', {'customer': customer})


def update(request, id):
    name = request.POST.get("name")
    cnpj = request.POST.get("cnpj")
    customer = Customer.objects.get(id=id)
    customer.name = name
    customer.cnpj = cnpj
    customer.save()
    return redirect(home)


def delete(request, id):
    customer = Customer.objects.get(id=id)
    customer.delete()
    return redirect(home)