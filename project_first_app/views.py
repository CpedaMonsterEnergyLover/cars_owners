from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView

from project_first_app.models import Owner, Car
from project_first_app.forms import AddOwnerForm, AddCarForm
import datetime


# Главная страница
def Mainpage(request):
    now = datetime.datetime.now()
    return render(request, 'welcome_page.html', {'time': now, 'abc': 123})


# Функционально: детальный просмотр данных owner по id
def OwnerDetail(request, id):
    try:
        p = Owner.objects.get(pk=id)
    except Owner.DoesNotExist:
        raise Http404("Owner does not exist")
    return render(request, 'owner.html', {'owner': p})


# Функционально: список всех owner
def OwnersList(request):
    context = {"dataset": Owner.objects.all()}
    return render(request, 'owners_list.html', context)


# Функционально: добавление owner
def AddOwner(request):
    context = {}
    form = AddOwnerForm(request.POST or None)
    if form.is_valid():
        form.save()
    context['form'] = form
    # т.к. представление функциональное, нет success_url
    return render(request, "add_owner.html", context)


# Функционально: добавление car
# def AddCar(request):
#    context = {}
#    form = AddCarForm(request.POST or None)
#    if form.is_valid():
#        form.save()
#    context['form'] = form
#    return render(request, "add_car.html", context)


# На основе классов: добавить car
class AddCar(CreateView):
    model = Car
    template_name = 'add_car.html'
    success_url = 'http://127.0.0.1:8000/car/list'
    fields = ['brand', 'model', 'color', 'number']


# На основе классов: удалить car
class DeleteCar(DeleteView):
    model = Car
    template_name = 'car_delete.html'
    success_url = "http://127.0.0.1:8000/car/list"


# На основе классов: изменить car
class UpdateCar(UpdateView):
    model = Car
    fields = ['brand', 'model', 'color', 'number']
    success_url = 'http://127.0.0.1:8000/car/list'
    template_name = 'car_update.html'


# На основе классов: список всех car
class CarsList(ListView):
    model = Car
    template_name = 'car_list.html'


# На основе классов: просмотр car по айди
class CarDetail(DetailView):
    model = Car
    template_name = 'car.html'
