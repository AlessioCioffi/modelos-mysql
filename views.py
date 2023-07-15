from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Teacher



# Create your views here.
    
class TeachersView(ListView):
    
    model = Teacher
    template_name = 'teachers/list.html'
    context_object_name = 'teachers'
    
    
class TeacherView(DetailView):
    
    model = Teacher
    template_name = 'teachers/detail.html'
    context_object_name = 'teacher'
    
    
class CreateTeacher(CreateView):
    
    model = Teacher
    template_name = 'teachers/create.html'
    fields = ['name','surname','telephone']
    success_url = reverse_lazy('home')
    
    
class UpdateTeacher(UpdateView):
    
    model = Teacher
    template_name = 'teachers/update.html'
    fields = ['name','surname','telephone']
    success_url = reverse_lazy('home')
    
    
class DeleteTeacher(DeleteView):
    
    model = Teacher
    template_name = 'teachers/delete.html'
    context_object_name = 'teacher'
    success_url = reverse_lazy('home')