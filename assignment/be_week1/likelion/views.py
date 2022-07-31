from django.shortcuts import render
from django.views.generic import CreateView, ListView, DetailView, DeleteView, UpdateView
from .models import LikeLion
# Create your views here.

class LikeLionCreateView(CreateView):
    model = LikeLion
    fields = "__all__"
    #fiels = ['name',]
    success_url = "/likelion"

class LikeLionListView(ListView):
    model = LikeLion
    paginate_by = 30
    ordering = ['name'] #이름순으로 배열

class LikeLionUpdateView(UpdateView):
    model = LikeLion
    fields = "__all__"
    template_name_suffix = "_update_form"
    success_url = "/likelion"

class LikeLionDeleteView(DeleteView):
    model = LikeLion
    success_url = "/likelion"

class LikeLionDetailView(DetailView):
    model = LikeLion
    success_url = "/likelion"