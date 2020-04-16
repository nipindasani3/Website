from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('table',views.table,name='table'),
    path('bar',views.bar_graph,name='bar_graph'),
    path('line',views.line_graph,name='line_graph'),
    path('pie',views.pie_graph,name='pie_graph'),
]