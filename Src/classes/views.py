from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request, param):
    return HttpResponse(f"hello, {param}")

def class_retrieve(request, class_name):
    context = {
        "title" : class_name,
        "description" : "This is a class description",
    }
    return render(request, "classes/index.html", context)