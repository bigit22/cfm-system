from django.shortcuts import render


def transactions_home(request):
    return render(request, 'cfm/home.html')
