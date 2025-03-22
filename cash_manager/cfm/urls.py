from django.urls import path
from . import views

urlpatterns = [
    path('', views.transactions_home, name='transactions_home'),
]