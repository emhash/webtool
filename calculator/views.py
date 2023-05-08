from django.shortcuts import render

# Create your views here.
def calchome(request):

    return render(request, 'calc.html')