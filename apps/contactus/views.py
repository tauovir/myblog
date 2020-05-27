
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
from apps.contactus.models import Contactus
from apps.blog.models import About

from django.conf import settings
import json
# from ..errorMessage import getApiMsg
import re 
# from ..utility import utils
from apps.contactus.forms import ContactusForm
# from contactus.models import Contactus,About
from django.contrib import messages
from django.views import View
from utilities.emailUtills import sendMail
# Create your views here.

# Class Based view
class ContactForm(View):
  template_name = 'contactus/contactus.html'
  def get(self, request):
    aboutData = About.objects.first()
    form = ContactusForm()
    return render(request, self.template_name, {'form': form,'aboutData' : aboutData})

  def post(self, request):
     # create a form instance and populate it with data from the request:
        form = ContactusForm(request.POST)
         # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            cleanedData = form.cleaned_data
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Thank you for contacting us')
            # redirect to a new URL:
            sendMail(cleanedData['name'],cleanedData['email'],'Contact us',cleanedData['message'])
            return redirect('contactus')

        
