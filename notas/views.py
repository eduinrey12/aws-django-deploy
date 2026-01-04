from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Nota

class NotaList(ListView):
    model = Nota
    template_name = 'nota_list.html'

class NotaCreate(CreateView):
    model = Nota
    fields = ['titulo', 'contenido']
    template_name = 'nota_form.html'
    success_url = reverse_lazy('nota_list')

class NotaUpdate(UpdateView):
    model = Nota
    fields = ['titulo', 'contenido']
    template_name = 'nota_form.html'
    success_url = reverse_lazy('nota_list')

class NotaDelete(DeleteView):
    model = Nota
    template_name = 'nota_confirm_delete.html'
    success_url = reverse_lazy('nota_list')