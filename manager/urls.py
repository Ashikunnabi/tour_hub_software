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
from .views import ( index, client_marketing, payment,
                     client_add, client_details, client_delete,  
                     enquiry_client_add, enquiry_client_details, enquiry_client_delete,  
                     air_ticket_add, air_ticket_details, air_ticket_delete,  
                     islamic_add, islamic_details, islamic_delete,  
                     tour_add,  tour_details,  tour_delete,  
                     visa_add, visa_details, visa_delete,
                     package_tour, package_tour_add, package_tour_details, package_tour_delete,
                     package_islamic, package_islamic_add, package_islamic_details, package_islamic_delete,
                     package_air_ticket, package_air_ticket_add, package_air_ticket_details, package_air_ticket_delete,
                     package_visa, package_visa_add, package_visa_details, package_visa_delete,
                    )
urlpatterns = [
    path('', index, name='m_index'),
    path('marketing', client_marketing, name='m_client_marketing'),
    path('payment', payment, name='m_payment'),
    
    path('client/add', client_add, name='m_client_add'),
    path('client/details/<int:id>', client_details, name='m_client_details'),
    path('client/delete/<int:id>', client_delete, name='m_client_delete'),
    
    path('enquiry_client/add', enquiry_client_add, name='m_enquiry_client_add'),
    path('enquiry_client/details/<int:id>', enquiry_client_details, name='m_enquiry_client_details'),
    path('enquiry_client/delete/<int:id>', enquiry_client_delete, name='m_enquiry_client_delete'),
    
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
]

