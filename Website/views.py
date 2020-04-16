from django.http import JsonResponse
from django.shortcuts import render
from Website.models import Olympics
from django.core import serializers

def info(request):
    dataset = Olympics.objects.all()
    data = serializers.serialize('json', dataset)
    return JsonResponse(data, safe=False)

def home(request):
    return render(request,'index.html')

def table(request):
    return render(request,'index.html')

def bar_graph(request):
    return render(request,'bar.html')

def line_graph(request):
    return render(request,'line.html')

def pie_graph(request):
    return render(request,'pie.html')