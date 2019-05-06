"""tour_hub_bd URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from .views import ( index, client_marketing, payment, request_custom_package,
                     client_add, client_details, client_delete, payment_details, 
                     enquiry_client_add, enquiry_client_details, enquiry_client_delete,  
                     air_ticket_add, air_ticket_details, air_ticket_delete,  
                     air_port_add, air_port_details, air_port_delete,  
                     islamic_add, islamic_details, islamic_delete,  order,
                     tour_add,  tour_details,  tour_delete,  cart_details, cart_delete,
                     visa_add, visa_details, visa_delete,
                     package_tour, package_tour_add, package_tour_details, package_tour_delete,
                     package_islamic, package_islamic_add, package_islamic_details, package_islamic_delete,
                     package_air_ticket, package_air_ticket_add, package_air_ticket_details, package_air_ticket_delete,
                     package_visa, package_visa_add, package_visa_details, package_visa_delete,
                     expenditure_add, expenditure_details, expenditure_delete,invoice,specific_invoice,
                    )
urlpatterns = [
    path('', index, name='e_index'),
    path('marketing', client_marketing, name='e_client_marketing'),
    path('payment', payment, name='e_payment'),
    path('payment/details/<int:id>', payment_details, name='e_payment_details'),
    
    path('request', request_custom_package, name='e_request_custom_package'),
    path('cart/details', cart_details, name='e_cart_details'),
    path('cart/delete/<int:id>', cart_delete, name='e_cart_delete'),
    
    path('order', order, name='e_order'),
    path('invoice', invoice, name='e_invoice'),     
    path('specific-invoice/<int:id>', specific_invoice, name='e_specific_invoice'),     
    
    path('client/add', client_add, name='e_client_add'),
    path('client/details/<int:id>', client_details, name='e_client_details'),
    path('client/delete/<int:id>', client_delete, name='e_client_delete'),
    
    path('enquiry_client/add', enquiry_client_add, name='e_enquiry_client_add'),
    path('enquiry_client/details/<int:id>', enquiry_client_details, name='e_enquiry_client_details'),
    path('enquiry_client/delete/<int:id>', enquiry_client_delete, name='e_enquiry_client_delete'),
    
    path('air-port/add', air_port_add, name='e_air_port_add'),
    path('air-port/details/<int:id>', air_port_details, name='e_air_port_details'),
    path('air-port/delete/<int:id>', air_port_delete, name='e_air_port_delete'),
    
    path('air-ticket/add', air_ticket_add, name='e_air_ticket_add'),
    path('air-ticket/details/<int:id>', air_ticket_details, name='e_air_ticket_details'),
    path('air-ticket/delete/<int:id>', air_ticket_delete, name='e_air_ticket_delete'),
    
    path('islamic/add', islamic_add, name='e_islamic_add'),
    path('islamic/details/<int:id>', islamic_details, name='e_islamic_details'),
    path('islamic/delete/<int:id>', islamic_delete, name='e_islamic_delete'),
    
    path('tour/add', tour_add, name='e_tour_add'),
    path('tour/details/<int:id>', tour_details, name='e_tour_details'),
    path('tour/delete/<int:id>', tour_delete, name='e_tour_delete'),
    
    path('visa/add', visa_add, name='e_visa_add'),
    path('visa/details/<int:id>', visa_details, name='e_visa_details'),
    path('visa/delete/<int:id>', visa_delete, name='e_visa_delete'),
    
    path('package-tour', package_tour, name='e_package_tour'),
    path('package-tour/add/<int:id>', package_tour_add, name='e_package_tour_add'),
    path('package-tour/details/<int:id>', package_tour_details, name='e_package_tour_details'),
    path('package-tour/delete/<int:id>', package_tour_delete, name='e_package_tour_delete'),
    
    path('package-islamic', package_islamic, name='e_package_islamic'),
    path('package-islamic/add/<int:id>', package_islamic_add, name='e_package_islamic_add'),
    path('package-islamic/details/<int:id>', package_islamic_details, name='e_package_islamic_details'),
    path('package-islamic/delete/<int:id>', package_islamic_delete, name='e_package_islamic_delete'),
    
    path('package-air-ticket', package_air_ticket, name='e_package_air_ticket'),
    path('package-air-ticket/add/<int:id>', package_air_ticket_add, name='e_package_air_ticket_add'),
    path('package-air-ticket/details/<int:id>', package_air_ticket_details, name='e_package_air_ticket_details'),
    path('package-air-ticket/delete/<int:id>', package_air_ticket_delete, name='e_package_air_ticket_delete'),
    
    path('package-visa', package_visa, name='e_package_visa'),
    path('package-visa/add/<int:id>', package_visa_add, name='e_package_visa_add'),
    path('package-visa/details/<int:id>', package_visa_details, name='e_package_visa_details'),
    path('package-visa/delete/<int:id>', package_visa_delete, name='e_package_visa_delete'),
    
    
    path('expenditure/add', expenditure_add, name='e_expenditure_add'),
    path('expenditure/details/<int:id>', expenditure_details, name='e_expenditure_details'),
    path('expenditure/delete/<int:id>', expenditure_delete, name='e_expenditure_delete'),
]

