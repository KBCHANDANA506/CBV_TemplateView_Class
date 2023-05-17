from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from app.forms import *
from django.http import HttpResponse

class cbv_context(TemplateView):
    template_name='cbv_context.html'
    def get_context_data(self,**kwargs):
        EDCO=super().get_context_data(**kwargs)
        EDCO['name']='Chandana'
        EDCO['age']=22
        return EDCO

class cbv_form(TemplateView):
    template_name='cbv_form.html'
    def get_context_data(self,**kwargs):
        EDCO=super().get_context_data(**kwargs)
        EDCO['TFO']=TopicForm()
        return EDCO
    def post(self,request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
        return HttpResponse("data submitted successfully....")
        