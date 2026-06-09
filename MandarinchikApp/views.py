from django.shortcuts import render

# Create your views here.
def menu(request):
    return render(request, 'menu.html')

def normal(request):
    return render(request, 'normal.html')