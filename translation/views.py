from django.shortcuts import render


# Create your views here.
def translate(request):
    return render(request, 'main.html')