from django.shortcuts import render

def greeting(request):
    return render(request, 'homepage.html')
