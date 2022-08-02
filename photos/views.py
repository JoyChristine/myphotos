from django.http import HttpResponse
from django.shortcuts import render
from .models import  * 
# Create your views here.
def welcome(request):
    images = image.objects.all()
    if request.method == 'GET':
        context = {'images': images}
        return render(request, 'all/index.html',context)