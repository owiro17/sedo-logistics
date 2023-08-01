from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from phonenumbers import PhoneNumberFormat, NumberParseException
import phonenumbers
User = get_user_model()

class ContactForm(forms.Form):
    first_name = forms.CharField(label="First Name", widget=forms.TextInput(attrs={'class': 'input'}))
    second_name = forms.CharField(label="Second Name", widget=forms.TextInput(attrs={'class':'input'}))
    email = forms.CharField(label="email " ,widget=forms.EmailInput(attrs={'class':'input'}))
    phone = forms.CharField(label="Phone",widget=forms.TextInput(attrs={'class': 'input'}))
    message = forms.CharField(label="Message", widget=forms.Textarea(attrs={'class':'message-box'}))
    road_freight = forms.CharField(label="Road Freight", widget=forms.CheckboxInput(attrs={'class':'checkbox'}),required=False)
    air_freight = forms.CharField(label="Air Freight", widget=forms.CheckboxInput(attrs={'class':'checkbox'}),required=False)
    sea_freight = forms.CharField(label="Sea Freight", widget=forms.CheckboxInput(attrs={'class':'checkbox'}),required=False)
    rail_freight = forms.CharField(label="Rail Freight", widget=forms.CheckboxInput(attrs={'class':'checkbox'}),required=False)
    customs_clearance = forms.CharField(label="Customs Clearance", widget=forms.CheckboxInput(attrs={'class':'checkbox'}),required=False)
    warehouse_management = forms.CharField(label="Warehouse Management", widget=forms.CheckboxInput(attrs={'class':'checkbox'}),required=False)
    project_logistics = forms.CharField(label="Project Logistics", widget=forms.CheckboxInput(attrs={'class':'checkbox'}),required=False)
    cargo_insuarance = forms.CharField(label="Cargo Insuarance", widget=forms.CheckboxInput(attrs={'class':'checkbox'}),required=False)
    remove_relocation = forms.CharField(label="Removal & Relocation", widget=forms.CheckboxInput(attrs={'class':'checkbox'}),required=False)
    other = forms.CharField(label="Not sure(advice accordingly)", widget=forms.CheckboxInput(attrs={'class':'checkbox'}),required=False)
    radio = forms.RadioSelect()
    description = forms.Textarea()
    def clean_ContactForms(self):
        data = self.cleaned_data["ContactForms"]
    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        # Add your validation logic here
        if len(first_name) < 2:
            raise ValidationError("First name should be at least 2 characters long.")
        return first_name
    def clean_second_name(self):
        second_name = self.cleaned_data['second_name']
        if len(second_name) < 2 :
            raise ValidationError("Second name should be at least 2 characters long.")
        return second_name
    def clean_phone(self):
        phone = self.cleaned_data['phone']

        try:
            # Parse the phone number
            parsed_phone = phonenumbers.parse(phone, None)

            # Check if the parsed phone number is valid
            if not phonenumbers.is_valid_number(parsed_phone):
                raise forms.ValidationError("Please enter a valid phone number. eg(+254712345678)")

            # Format the phone number in the desired format
            formatted_phone = phonenumbers.format_number(parsed_phone, PhoneNumberFormat.E164)

            # Update the cleaned data with the formatted phone number
            self.cleaned_data['phone'] = formatted_phone

        except NumberParseException:
            raise forms.ValidationError("Please enter a valid phone number.")

        return phone
    def clean(self):
        cleaned_data = super().clean()
        # Add any cross-field validation logic here
        
        return cleaned_data