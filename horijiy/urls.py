from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('export/', views.export_to_excel, name='export_to_excel'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
   # path('logout', auth_views.LogoutView.as_view(), {'next_page': 'login/?next=/'}, name='logout'),
    path('', auth_views.LogoutView.as_view(next_page='/login/'), name='logout'),
    # Boshqa yo'nalishlar...
]
