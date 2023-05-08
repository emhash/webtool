from django.shortcuts import render

# Create your views here.
def bhome(request):
    return render(request, 'bmi.html')




#  404 not found
def notfound(request , exception):
    return render(request, '404/notfound1.html')

