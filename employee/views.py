from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DeleteView,UpdateView,DetailView, ListView
from django.urls import reverse_lazy

from .models import Employee
# Create your views here.
@login_required
def home(request):
    context ={}
    return render(request, 'employee/home.html',context)

class AddEmployeeVIew(LoginRequiredMixin,CreateView):
    template_name = "employee/add_employee.html"
    model = Employee
    fields ="__all__"
    success_url = reverse_lazy('list-employee')

class EmployeeListView(LoginRequiredMixin, ListView):
    template_name ="employee/list_employee.html"
    context_object_name="employees"
    queryset = Employee.objects.all()