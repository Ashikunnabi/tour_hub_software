from django import forms
from django.forms import ModelForm
from .models import Employee, Client, EnquiryClient, Marketing, AirPort, AirTicket, Islamic, Tour, Visa, PackageIslamic, PackageTour, PackageAirTicket, PackageVisa, Order, Expenditure


class EmployeeForm(ModelForm):
    class Meta:
        model   = Employee
        fields  = '__all__'        
        widgets = {
                'type'              : forms.Select(attrs={'class':'custom-select'}),
                'employee_id'       : forms.TextInput(attrs={'class':'form-control'}),
                'name'              : forms.TextInput(attrs={'class':'form-control'}),
                'password'          : forms.TextInput(attrs={'class':'form-control'}),
                'phone_number'      : forms.TextInput(attrs={'class':'form-control'}),
                'email'             : forms.EmailInput(attrs={'class':'form-control'}),
                'present_address'   : forms.TextInput(attrs={'class':'form-control'}),
                'permanent_address' : forms.TextInput(attrs={'class':'form-control'}),
                'nid'               : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'dob'               : forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'designation'       : forms.TextInput(attrs={'class':'form-control'}),
                'photo'             : forms.FileInput(attrs={'class':'form-control'}),
                'marital_status'    : forms.Select(attrs={'class':'custom-select'}),
            }
            

class ClientForm(ModelForm):
    class Meta:
        model   = Client
        exclude  = ('created_by',)         
        widgets = {
                'name'              : forms.TextInput(attrs={'class':'form-control', 'onchange':'autoFill()'}),
                'phone'             : forms.TextInput(attrs={'class':'form-control', 'onchange':'autoFill()'}),
                'email'             : forms.EmailInput(attrs={'class':'form-control', 'onchange':'autoFill()'}),
                'profession'        : forms.TextInput(attrs={'class':'form-control', 'onchange':'autoFill()'}),
                'address'           : forms.TextInput(attrs={'class':'form-control', 'onchange':'autoFill()'}),
                'photo'             : forms.FileInput(attrs={'class':'form-control'}),
            }

            
class EnquiryClientForm(ModelForm):
    class Meta:
        model   = EnquiryClient
        exclude  = ('created_by',)   
        widgets = {
                'name'              : forms.TextInput(attrs={'id':'e_name', 'class':'form-control', 'onchange':'eautoFill()'}),
                'phone'             : forms.TextInput(attrs={'id':'e_phone', 'class':'form-control', 'onchange':'eautoFill()'}),
                'email'             : forms.EmailInput(attrs={'id':'e_email', 'class':'form-control', 'onchange':'eautoFill()'}),
                'profession'        : forms.TextInput(attrs={'id':'e_profession', 'class':'form-control', 'onchange':'eautoFill()'}),
                'address'           : forms.TextInput(attrs={'id':'e_address', 'class':'form-control', 'onchange':'eautoFill()'}),
                'photo'             : forms.FileInput(attrs={'class':'form-control'}),
                'type'              : forms.Select(attrs={'class':'custom-select'}),
                'country_name'      : forms.TextInput(attrs={'class':'form-control'}),
                'places'            : forms.TextInput(attrs={'class':'form-control'}),
                'members'           : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'child'             : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'infant'            : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'hotel_quality'     : forms.Select(attrs={'class':'custom-select'}),
                'number_of_rooms'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'airline'           : forms.TextInput(attrs={'class':'form-control'}),
                'duration'          : forms.TextInput(attrs={'class':'form-control',}),
                'by_air_route'      : forms.TextInput(attrs={'class':'form-control'}),
                'visa_detail'       : forms.Select(attrs={'class':'custom-select'}),
                'previous_tour'     : forms.TextInput(attrs={'class':'form-control'}),
                'special_requirment': forms.Textarea(attrs={'class':'form-control'}),
                'client_price'      : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'follow_up_date_01' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'update_01'         : forms.TextInput(attrs={'class':'form-control'}),
                'follow_up_date_02' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'update_02'         : forms.TextInput(attrs={'class':'form-control'}),
                'follow_up_date_03' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'update_03'         : forms.TextInput(attrs={'class':'form-control'}),
                'follow_up_date_04' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'update_04'         : forms.TextInput(attrs={'class':'form-control'}),
                'follow_up_date_05' : forms.DateInput(attrs={'class':'form-control','type':'date'}),
                'update_05'         : forms.TextInput(attrs={'class':'form-control'}),
                'status'            : forms.Select(attrs={'class':'custom-select'}),
                'reason_of_cancel'  : forms.TextInput(attrs={'class':'form-control'}),               
            }   
            
    
class AirPortForm(ModelForm):
    class Meta:
        model   = AirPort
        exclude  = ('created_by',)      
        widgets = {
                'name'       : forms.TextInput(attrs={'class':'form-control'}),
                'country'     : forms.TextInput(attrs={'class':'form-control'}),
            } 
            
    
class AirTicketForm(ModelForm):
    class Meta:
        model   = AirTicket
        exclude  = ('created_by',)      
        widgets = {
                'airline'       : forms.TextInput(attrs={'class':'form-control'}),
                'departure'     : forms.TextInput(attrs={'class':'form-control', 'list':'airports'}),
                'arrival'       : forms.TextInput(attrs={'class':'form-control', 'list':'airports'}),
                'quantity'      : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'actual_price'  : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'client_price'  : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }
            

class IslamicForm(ModelForm):
    class Meta:
        model   = Islamic
        exclude  = ('created_by',)      
        widgets = {
                'title'          : forms.TextInput(attrs={'class':'form-control'}),
                'type'           : forms.Select(attrs={'class':'custom-select'}),
                'places'         : forms.TextInput(attrs={'class':'form-control'}),
                'duration_days'  : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'duration_nights': forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'members'        : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'actual_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }


class TourForm(ModelForm):
    class Meta:
        model   = Tour
        exclude  = ('created_by',)       
        widgets = {
                'title'          : forms.TextInput(attrs={'class':'form-control'}),
                'type'           : forms.Select(attrs={'class':'custom-select'}),
                'places'         : forms.TextInput(attrs={'class':'form-control'}),
                'duration_days'  : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'duration_nights': forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'members'        : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'actual_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }


class VisaForm(ModelForm):
    class Meta:
        model   = Visa
        exclude  = ('created_by',)       
        widgets = {
                'country_name'   : forms.TextInput(attrs={'class':'form-control'}),
                'processing_time': forms.TextInput(attrs={'class':'form-control'}),
                'actual_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }           


class PackageTourForm(ModelForm):
    class Meta:
        model   = PackageTour
        exclude  = ('created_by','in_cart',)      
        widgets = {
                'client'         : forms.Select(attrs={'class':'custom-select chosen'}),
                'title'          : forms.TextInput(attrs={'class':'form-control'}),
                'type'           : forms.Select(attrs={'class':'custom-select'}),
                'places'         : forms.TextInput(attrs={'class':'form-control'}),
                'duration_days'  : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'duration_nights': forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'members'        : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'child'             : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'infant'            : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'hotel_quality'     : forms.Select(attrs={'class':'custom-select'}),
                'number_of_rooms'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'airline'           : forms.TextInput(attrs={'class':'form-control'}),
                'special_requirment': forms.Textarea(attrs={'class':'form-control'}),
                'actual_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }          


class PackageIslamicForm(ModelForm):
    class Meta:
        model   = PackageIslamic
        exclude  = ('created_by','in_cart',)   
        widgets = {
                'client'         : forms.Select(attrs={'class':'custom-select chosen'}),
                'title'          : forms.TextInput(attrs={'class':'form-control'}),
                'type'           : forms.Select(attrs={'class':'custom-select'}),
                'places'         : forms.TextInput(attrs={'class':'form-control'}),
                'duration_days'  : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'duration_nights': forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'members'        : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'child'             : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'infant'            : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'hotel_quality'     : forms.Select(attrs={'class':'custom-select'}),
                'number_of_rooms'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'airline'           : forms.TextInput(attrs={'class':'form-control'}),
                'special_requirment': forms.Textarea(attrs={'class':'form-control'}),
                'actual_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }


class PackageAirTicketForm(ModelForm):
    class Meta:
        model   = PackageAirTicket
        exclude  = ('created_by','in_cart',)
        widgets = {
                'client'        : forms.Select(attrs={'class':'custom-select chosen'}),
                'airline'       : forms.TextInput(attrs={'class':'form-control'}),
                'departure'     : forms.TextInput(attrs={'class':'form-control', 'list':'airports'}),
                'arrival'       : forms.TextInput(attrs={'class':'form-control', 'list':'airports'}),
                'actual_price'  : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'quantity'      : forms.NumberInput(attrs={'class':'form-control','min':'1'}),
                'client_price'  : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }


class PackageVisaForm(ModelForm):
    class Meta:
        model   = PackageVisa
        exclude  = ('created_by','in_cart',)   
        widgets = {
                'client'         : forms.Select(attrs={'class':'custom-select chosen'}),
                'country_name'   : forms.TextInput(attrs={'class':'form-control'}),
                'processing_time': forms.TextInput(attrs={'class':'form-control'}),
                'actual_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'client_price'   : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }           


class OrderForm(ModelForm):
    class Meta:
        model   = Order
        exclude  = ('created_by','client','package_tour','package_islamic','package_air_ticket','package_visa',)   
        widgets = {
                'payment_method'     : forms.Select(attrs={'class':'custom-select'}),
                'cheque_number'      : forms.TextInput(attrs={'class':'form-control'}),
                'bank'               : forms.TextInput(attrs={'class':'form-control'}),
                'branch'             : forms.TextInput(attrs={'class':'form-control'}),
                'cheque_date'        : forms.TextInput(attrs={'class':'form-control'}),
                'booking_id'         : forms.TextInput(attrs={'class':'form-control'}),
                'actual_price'       : forms.NumberInput(attrs={'class':'form-control','min':'0'}),                
                'total_ammount'      : forms.NumberInput(attrs={'class':'form-control','min':'0'}),                
                'discount'           : forms.NumberInput(attrs={'class':'form-control','min':'0'}),                
                'tax_rate'           : forms.TextInput(attrs={'class':'form-control'}),                
                'total_tax'          : forms.NumberInput(attrs={'class':'form-control','min':'0'}),                
                'shipping_handling'  : forms.NumberInput(attrs={'class':'form-control','min':'0'}),                
                'payable_ammount'    : forms.NumberInput(attrs={'class':'form-control','min':'0','onkeyup':'calculation()'}),                
                'received_ammount'   : forms.NumberInput(attrs={'class':'form-control','min':'0','onkeyup':'calculation()'}),
                'due_ammount'        : forms.NumberInput(attrs={'class':'form-control','min':'0'}),                  
                'advertisement'      : forms.FileInput(attrs={'class':'form-control'}),
            }


class ExpenditureForm(ModelForm):
    class Meta:
        model   = Expenditure
        exclude  = ('created_at',)    
        widgets = {
                'made_by'      : forms.TextInput(attrs={'class':'form-control'}),
                'date'             : forms.TextInput(attrs={'class':'form-control','type':'date'}),
                'by'               : forms.Select(attrs={'class':'custom-select'}),
                'being_the'        : forms.TextInput(attrs={'class':'form-control'}),
                'description_01'   : forms.TextInput(attrs={'class':'form-control'}),
                'cost_01'          : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'description_02'   : forms.TextInput(attrs={'class':'form-control'}),
                'cost_02'          : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'description_03'   : forms.TextInput(attrs={'class':'form-control'}),
                'cost_03'          : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'description_04'   : forms.TextInput(attrs={'class':'form-control'}),
                'cost_04'          : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'description_05'   : forms.TextInput(attrs={'class':'form-control'}),
                'cost_05'          : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
                'total'            : forms.NumberInput(attrs={'class':'form-control','min':'0'}),
            }

            
            
            
            
            
            
            
            
            
            
            
            
            