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
from .views import ( employee_add, employee_details, employee_delete, 
                     index, client_marketing, payment, request_custom_package,
                     client_add, client_details, client_delete,  cart_details,
                     enquiry_client_add, enquiry_client_details, enquiry_client_delete,  
                     air_port_add, air_port_details, air_port_delete,  
                     air_ticket_add, air_ticket_details, air_ticket_delete,  
                     islamic_add, islamic_details, islamic_delete,  
                     tour_add,  tour_details,  tour_delete,  cart_delete,
                     visa_add, visa_details, visa_delete, order, payment_details,
                     package_tour, package_tour_add, package_tour_details, package_tour_delete,
                     package_islamic, package_islamic_add, package_islamic_details, package_islamic_delete,
                     package_air_ticket, package_air_ticket_add, package_air_ticket_details, package_air_ticket_delete,
                     package_visa, package_visa_add, package_visa_details, package_visa_delete,
                     expenditure_add, expenditure_details, expenditure_delete, invoice,specific_invoice,
                     client_marketing_more_email, client_marketing_delete_category, client_marketing_change_category,
                     client_marketing_delete_email, client_marketing_change_email
                    )
urlpatterns = [
    path('', index, name='m_index'),
    path('payment', payment, name='m_payment'),
    path('payment/details/<int:id>', payment_details, name='m_payment_details'),
    
    path('marketing', client_marketing, name='m_client_marketing'),
    path('marketing/add', client_marketing_more_email, name='m_client_marketing_more_email'),
    path('marketing/delete', client_marketing_delete_category, name='m_client_marketing_delete_category'),
    path('marketing/change', client_marketing_change_category, name='m_client_marketing_change_category'),
    
    path('marketing/email/delete', client_marketing_delete_email, name='m_client_marketing_delete_email'),
    path('marketing/email/change', client_marketing_change_email, name='m_client_marketing_change_email'),
    
    path('requests', request_custom_package, name='m_request_custom_package'),
    path('cart/details', cart_details, name='m_cart_details'),
    path('cart/delete/<int:id>', cart_delete, name='m_cart_delete'),
    
    path('order', order, name='m_order'),   
    path('invoice', invoice, name='m_invoice'),   
    path('specific-invoice/<int:id>', specific_invoice, name='m_specific_invoice'),  
    
    path('employee/add', employee_add, name='m_employee_add'),
    path('employee/details/<int:id>', employee_details, name='m_employee_details'),
    path('employee/delete/<int:id>', employee_delete, name='m_employee_delete'),
    
    path('client/add', client_add, name='m_client_add'),
    path('client/details/<int:id>', client_details, name='m_client_details'),
    path('client/delete/<int:id>', client_delete, name='m_client_delete'),
    
    path('enquiry_client/add', enquiry_client_add, name='m_enquiry_client_add'),
    path('enquiry_client/details/<int:id>', enquiry_client_details, name='m_enquiry_client_details'),
    path('enquiry_client/delete/<int:id>', enquiry_client_delete, name='m_enquiry_client_delete'),
    
    path('air-port/add', air_port_add, name='m_air_port_add'),
    path('air-port/details/<int:id>', air_port_details, name='m_air_port_details'),
    path('air-port/delete/<int:id>', air_port_delete, name='m_air_port_delete'),
    
    path('air-ticket/add', air_ticket_add, name='m_air_ticket_add'),
    path('air-ticket/details/<int:id>', air_ticket_details, name='m_air_ticket_details'),
    path('air-ticket/delete/<int:id>', air_ticket_delete, name='m_air_ticket_delete'),
    
    path('islamic/add', islamic_add, name='m_islamic_add'),
    path('islamic/details/<int:id>', islamic_details, name='m_islamic_details'),
    path('islamic/delete/<int:id>', islamic_delete, name='m_islamic_delete'),
    
    path('tour/add', tour_add, name='m_tour_add'),
    path('tour/details/<int:id>', tour_details, name='m_tour_details'),
    path('tour/delete/<int:id>', tour_delete, name='m_tour_delete'),
    
    path('visa/add', visa_add, name='m_visa_add'),
    path('visa/details/<int:id>', visa_details, name='m_visa_details'),
    path('visa/delete/<int:id>', visa_delete, name='m_visa_delete'),
    
    path('package-tour', package_tour, name='m_package_tour'),
    path('package-tour/add/<int:id>', package_tour_add, name='m_package_tour_add'),
    path('package-tour/details/<int:id>', package_tour_details, name='m_package_tour_details'),
    path('package-tour/delete/<int:id>', package_tour_delete, name='m_package_tour_delete'),
    
    path('package-islamic', package_islamic, name='m_package_islamic'),
    path('package-islamic/add/<int:id>', package_islamic_add, name='m_package_islamic_add'),
    path('package-islamic/details/<int:id>', package_islamic_details, name='m_package_islamic_details'),
    path('package-islamic/delete/<int:id>', package_islamic_delete, name='m_package_islamic_delete'),
    
    path('package-air-ticket', package_air_ticket, name='m_package_air_ticket'),
    path('package-air-ticket/add/<int:id>', package_air_ticket_add, name='m_package_air_ticket_add'),
    path('package-air-ticket/details/<int:id>', package_air_ticket_details, name='m_package_air_ticket_details'),
    path('package-air-ticket/delete/<int:id>', package_air_ticket_delete, name='m_package_air_ticket_delete'),
    
    path('package-visa', package_visa, name='m_package_visa'),
    path('package-visa/add/<int:id>', package_visa_add, name='m_package_visa_add'),
    path('package-visa/details/<int:id>', package_visa_details, name='m_package_visa_details'),
    path('package-visa/delete/<int:id>', package_visa_delete, name='m_package_visa_delete'),
    
    path('expenditure/add', expenditure_add, name='m_expenditure_add'),
    path('expenditure/details/<int:id>', expenditure_details, name='m_expenditure_details'),
    path('expenditure/delete/<int:id>', expenditure_delete, name='m_expenditure_delete'),
]

