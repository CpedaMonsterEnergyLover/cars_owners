from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('owner/<int:id>/', OwnerDetail),
    path('owner/list/', OwnersList),
    path('owner/new/', AddOwner),

    path('car/<int:pk>/', CarDetail.as_view()),
    path('car/list', CarsList.as_view()),
    path('car/<int:pk>/update', UpdateCar.as_view()),
    path('car/new/', AddCar.as_view()),
    path('car/<int:pk>/delete', DeleteCar.as_view()),



    path('', views.Mainpage),
]
