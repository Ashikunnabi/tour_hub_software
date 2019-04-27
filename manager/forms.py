from django import forms
from django.forms import ModelForm
from .models import Client, EnquiryClient, AirTicket, Islamic, Tour, Visa, PackageIslamic, PackageTour, PackageAirTicket, PackageVisa


class ClientForm(ModelForm):
    class Meta:
        model   = Client
        fields  = '__all__'        
        widgets = {
                'name'              : forms.TextInput(attrs={'class':'form-control', 'onchange':'autoFill()'}),
                'phone'             : forms.TextInput(attrs={'class':'form-control', 'onchange':'autoFill()'}),
                'email'             : forms.EmailInput(attrs={'class':'form-control', 'onchange':'autoFill()'}),
                'nid'               : forms.TextInput(attrs={'class':'form-control'}),
                'profession'        : forms.TextInput(attrs={'class':'form-control'}),
                'blood_group'       : forms.Select(attrs={'class':'custom-select'}),
                'present_address'   : forms.TextInput(attrs={'class':'form-control'}),
                'permanent_address' : forms.TextInput(attrs={'class':'form-control'}),
                'photo'             : forms.FileInput(attrs={'class':'form-control'}),
            }

class EnquiryClientForm(ModelForm):
    class Meta:
        model   = EnquiryClient
        fields  = '__all__'        
        widgets = {
                'name'              : forms.TextInput(attrs={'id':'e_name', 'class':'form-control', 'onchange':'eautoFill()'}),
                'phone'             : forms.TextInput(attrs={'id':'e_phone', 'class':'form-control', 'onchange':'eautoFill()'}),
                'email'             : forms.EmailInput(attrs={'id':'e_email', 'class':'form-control', 'onchange':'eautoFill()'}),
                'nid'               : forms.TextInput(attrs={'class':'form-control'}),
                'profession'        : forms.TextInput(attrs={'class':'form-control'}),
                'blood_group'       : forms.Select(attrs={'class':'custom-select'}),
                'present_address'   : forms.TextInput(attrs={'class':'form-control'}),
                'permanent_address' : forms.TextInput(attrs={'class':'form-control'}),
                'photo'             : forms.FileInput(attrs={'class':'form-control'}),
                'type'              : forms.Select(attrs={'class':'custom-select'}),
                'country_name'      : forms.TextInput(attrs={'class':'form-control'}),
                'places'            : forms.TextInput(attrs={'class':'form-control'}),
                'members'           : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'airline'           : forms.TextInput(attrs={'class':'form-control'}),
                'duration'          : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'client_price'      : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
            }


class AirTicketForm(ModelForm):
    class Meta:
        model   = AirTicket
        fields  = '__all__'        
        widgets = {
                'airline'       : forms.TextInput(attrs={'class':'form-control'}),
                'departure_from': forms.TextInput(attrs={'class':'form-control'}),
                'departure_to'  : forms.TextInput(attrs={'class':'form-control'}),
                'actual_price'  : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'client_price'  : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
            }
            

class IslamicForm(ModelForm):
    class Meta:
        model   = Islamic
        fields  = '__all__'        
        widgets = {
                'title'          : forms.TextInput(attrs={'class':'form-control'}),
                'type'           : forms.Select(attrs={'class':'custom-select'}),
                'places'         : forms.TextInput(attrs={'class':'form-control'}),
                'duration_days'  : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'duration_nights': forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'members'        : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'actual_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
            }


class TourForm(ModelForm):
    class Meta:
        model   = Tour
        fields  = '__all__'        
        widgets = {
                'title'          : forms.TextInput(attrs={'class':'form-control'}),
                'type'           : forms.Select(attrs={'class':'custom-select'}),
                'places'         : forms.TextInput(attrs={'class':'form-control'}),
                'duration_days'  : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'duration_nights': forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'members'        : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'actual_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
            }


class VisaForm(ModelForm):
    class Meta:
        model   = Visa
        fields  = '__all__'        
        widgets = {
                'country_name'   : forms.TextInput(attrs={'class':'form-control'}),
                'processing_time': forms.TextInput(attrs={'class':'form-control'}),
                'actual_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
            }           


class PackageTourForm(ModelForm):
    class Meta:
        model   = PackageTour
        fields  = '__all__'        
        widgets = {
                'client'         : forms.Select(attrs={'class':'custom-select'}),
                'title'          : forms.TextInput(attrs={'class':'form-control'}),
                'type'           : forms.Select(attrs={'class':'custom-select'}),
                'places'         : forms.TextInput(attrs={'class':'form-control'}),
                'duration_days'  : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'duration_nights': forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'members'        : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'paid_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'due_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }          


class PackageIslamicForm(ModelForm):
    class Meta:
        model   = PackageIslamic
        fields  = '__all__'        
        widgets = {
                'client'         : forms.Select(attrs={'class':'custom-select'}),
                'title'          : forms.TextInput(attrs={'class':'form-control'}),
                'type'           : forms.Select(attrs={'class':'custom-select'}),
                'places'         : forms.TextInput(attrs={'class':'form-control'}),
                'duration_days'  : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'duration_nights': forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'members'        : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'paid_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'due_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }


class PackageAirTicketForm(ModelForm):
    class Meta:
        model   = PackageAirTicket
        fields  = '__all__'        
        widgets = {
                'client'        : forms.Select(attrs={'class':'custom-select'}),
                'airline'       : forms.TextInput(attrs={'class':'form-control'}),
                'departure_from': forms.TextInput(attrs={'class':'form-control'}),
                'departure_to'  : forms.TextInput(attrs={'class':'form-control'}),
                'client_price'  : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'paid_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'due_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }


class PackageVisaForm(ModelForm):
    class Meta:
        model   = PackageVisa
        fields  = '__all__'        
        widgets = {
                'client'         : forms.Select(attrs={'class':'custom-select'}),
                'country_name'   : forms.TextInput(attrs={'class':'form-control'}),
                'processing_time': forms.TextInput(attrs={'class':'form-control'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'paid_price'   : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'due_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }           
