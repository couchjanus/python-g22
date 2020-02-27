# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
# def index(request):
#     return HttpResponse("Hello, world. You're at the MyCompany Home Page.")

def index(request):
    template = loader.get_template('employee/index.html')
    context = {
        'title': 'My Compant Home Page',
    }
    return HttpResponse(template.render(context, request))
