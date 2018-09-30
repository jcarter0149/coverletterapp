# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import *

def PersonFormView(request):
    if request.method == 'GET':
        person_form = PersonForm() 
        template_name = 'personform.html'
        return render(request, template_name, {'person_form': person_form}) 
    
    elif request.method == 'POST':
        form = PersonForm(request.POST)
        form.data = request.POST
        form.save()
        return  HttpResponseRedirect(reverse('coverletter:coverletter'))
        

def CoverLetterView(request):
    info = PersonInfo.objects.latest('id')
    return render(request, 'coverletter.html', {'info': info})


