from django.shortcuts import render

def custom_home(request):
    return render(request, 'home.html')