# http-responses to http-requests of users

from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, HttpResponseNotFound
from .forms import UserForm
from .models import Person

# Create your views here.

def index(request):
    return render(request, 'index.html')

def static(request):
    context = {'age': 10, 'cat': ['Ноутбуки', 'Принтеры', 'Сканреы']}
    return render(request, 'static.html', context=context)

def dynamic(request):

    #заполнение формы
    if request.method == "POST":
        name = request.POST.get("name")
        age = request.POST.get("age")
        comment = request.POST.get("comment")
        output = f"<h2> Пользователь </h2> <h3> Имя - {name} <br> Возраст - {age} <br> Комментарий: {comment}</h3>"
        return HttpResponse(output)
    #получение формы
    else:
        userform = UserForm()
        return render(request, 'dynamic.html', {"form" : userform})
    
def create(request):
    if request.method == "POST":
        person = Person()
        person.name = request.POST.get("name")
        person.age = request.POST.get("age")
        person.save()
    return HttpResponseRedirect('/show_people')

def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == 'POST':
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect('/show_people')
        else:
            return render(request, 'edit.html', {'person':person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2> Клиент не найден </h2>")
    
def delete (request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect('/show_people')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2> Клиент не найден </h2>")
    
def show_people(request):
    people = Person.objects.all()
    return render(request, 'show_people.html', {"people":people})

# ____________________________________________________

def details(request):
    return HttpResponsePermanentRedirect('/') #перенаправление в корень постоянное