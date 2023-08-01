from django.shortcuts import render
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django import forms
from django.core.exceptions import ValidationError
from .forms import ContactForm
from django.contrib import messages

# Create your views here.
def index(request):
   return render(request, "index.html",{})

def about_us(request):
    return render(request, "about-us.html",{})

# -------------------------------- phase 2-----------------------------------------------   
# def ourservices(request):
#    return render(request, "ourservices.html",{})
# def login(request):
#    return render(request, "login.html",{})
# def signup(request):
#    return render(request, "sign-up.html",{})
# --------------------------------------------------------------------------------
def contactUs(request):
   form = ContactForm(request.POST or None)

   if request.method == 'POST':
      form = ContactForm(request.POST or None)
      if form.is_valid():
         # Get form data
         first_name = form.cleaned_data['first_name']
         second_name = form.cleaned_data['second_name']
         email = form.cleaned_data['email']
         phone = form.cleaned_data['phone']
         message = form.cleaned_data['message']
         road_freight = form.cleaned_data['road_freight']
         air_freight =  form.cleaned_data['air_freight']
         sea_freight = form.cleaned_data['sea_freight']
         rail_freight = form.cleaned_data['rail_freight']
         warehouse_management = form.cleaned_data['warehouse_management']
         project_logistics = form.cleaned_data['project_logistics']
         cargo_insuarance = form.cleaned_data['cargo_insuarance']
         remove_relocation = form.cleaned_data['remove_relocation']
         other= form.cleaned_data['other']
         customs_clearance = form.cleaned_data['customs_clearance']
         checked_checkboxes = []
         checkbox_fields = [
            'road_freight', 'air_freight', 'sea_freight', 'rail_freight',
            'customs_clearance', 'warehouse_management', 'project_logistics',
            'cargo_insuarance', 'remove_relocation', 'other'
         ]
         for field_name in checkbox_fields:
            if form.cleaned_data[field_name] == "True":
               checked_checkboxes.append(field_name)
         if not any(checked_checkboxes):
            messages.error(request, "You must check at least one service")
         else:
            messages.success(request, 'Form submitted successfully!')

         subject = f"NEW CLIENT FORM SUBBMISSION FROM {first_name} {second_name}"
         body = f"Client Name: {first_name} {second_name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}\n Service{checked_checkboxes}"
         sender_email = f"{email}"  # Replace with your email
         receiver_email = ["info@sedologistics.co.ke"]  # Replace with the recipient's email
         # send_mail(subject, body, sender_email, [receiver_email],fail_silently=False,headers={"Importance": "high"})
         email = EmailMessage(subject,body,sender_email,receiver_email, headers={'X-Priority': '1'})
         email.send()
         print(form.cleaned_data)
   return render(request, "contact-us.html",{'form':form})
def air_frieght(request):
   return render(request, "air-freight.html",{})

def road_frieght(request):
   return render(request, "road-freight.html",{})

def rail_frieght(request):
   return render(request, "rail-freight.html",{})

def sea_frieght(request):
   return render(request, "sea-freight.html",{})

def cargo_insuarance(request):
   return render(request, "cargo-insuarance.html",{})

def customs_clearance(request):
   return render(request, "customs-clearance.html",{})

def project_logistics(request):
   return render(request, "project-logistics.html",{})

def warehouse_management(request):
   return render(request, "warehouse-management.html")

def removal(request):
   return render(request, "removal-and-relocation.html")

   return render(request, "contact-us.html",{'form':form})