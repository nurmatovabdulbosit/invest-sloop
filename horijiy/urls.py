from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('export/', views.export_to_excel, name='export_to_excel'),
    # Boshqa yo'nlashlar...
]
