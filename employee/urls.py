from django.urls import path
from . import views

urlpatterns = [
    path('home', views.home , name='home'),
    path('add-employee', views.AddEmployeeVIew.as_view(), name='add-employee'),
    path('list-employee', views.EmployeeListView.as_view(), name='list-employee'),
    path('delete/<int:pk>', views.EmployeeDeleteView.as_view(), name='delete-employee'),
    path('update/<int:pk>', views.EmployeeUpdateView.as_view(), name='update-employee'),
]