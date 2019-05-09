from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.models import Group, User
from django.contrib.auth.decorators import login_required

from authentication.decorators import has_access
from .forms import (  EmployeeForm, ClientForm, EnquiryClientForm, AirTicketForm, AirPortForm, 
                      IslamicForm, TourForm, VisaForm, OrderForm,
                      PackageTourForm, PackageIslamicForm, ExpenditureForm,
                      PackageAirTicketForm, PackageVisaForm,
                   )
from manager.models import ( Employee, Client, EnquiryClient, AirTicket, AirPort, 
                      Islamic, Tour, Visa, Cart, Order,
                      PackageTour, PackageIslamic, Expenditure,
                      PackageAirTicket, PackageVisa,
                    )

@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def index(request):
    """  Manager's Dashboard """    
    clients        = Client.objects.all()
    
    context = {
        'clients': clients,
        'total_packages': package_count(),
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/index.html', context)

      
def package_count():
    """ Generating the total package available to use """   
    tours          = Tour.objects.all()
    islamics       = Islamic.objects.all()
    air_tickets    = AirTicket.objects.all()
    visas          = Visa.objects.all() 
    count = 0
    
    for i in tours:
        count = count + 1
    for i in islamics:
        count = count + 1
    for i in air_tickets:
        count = count + 1
    for i in visas:
        count = count + 1
        
    return count


@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def client_add(request):
    """  Add new client and see the list of clients """
    success_message, error_message = None, None
    form            = ClientForm
    clients         = Client.objects.all()
    enquiry_form    = EnquiryClientForm
    enquiry_clients = EnquiryClient.objects.all()
    
    if request.method=="POST":
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            obj.save()
            success_message = "added a new client"
        else:
            error_message = "to add a new client"
            
    context = {
        'form'           : form,
        'enquiry_form'   : enquiry_form,
        'clients'        : clients,
        'enquiry_clients': enquiry_clients,
        'success_message': success_message,
        'error_message'  : error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/client_add.html', context)


@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def client_details(request,id):
    """  view and update a client depending on id """
    success_message, error_message = None, None  
    client = get_object_or_404(Client, id=id)
    form   = ClientForm(instance=client)
    # All packages taken by a specific user    
    package_tours       = PackageTour.objects.filter(client__id=id)
    package_islamics    = PackageIslamic.objects.filter(client__id=id)
    package_air_tickets = PackageAirTicket.objects.filter(client__id=id)
    package_visas       = PackageVisa.objects.filter(client__id=id)
    
    if request.method=="POST":
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            success_message = "updated client"
        else:
            error_message = "to update client"
            
    context = {
        'form'               : form,
        'client'             : client,
        'package_tours'      : package_tours,
        'package_islamics'   : package_islamics,
        'package_air_tickets': package_air_tickets,
        'package_visas'      : package_visas,
        'success_message'    : success_message,
        'error_message'      : error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/client_details.html', context)


@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def client_delete(request,id):
    """  delete a specific client depending on id """
    success_message, error_message = None, None
    form            = ClientForm()    
    client          = get_object_or_404(Client, id=id)
    clients         = Client.objects.all()
    enquiry_form    = EnquiryClientForm
    enquiry_clients = EnquiryClient.objects.all()
    
    if request.method=="POST":
        client.delete()
        success_message = "deleted client"
    else:
        error_message = "to delete client"
        
    context = {
        'form'           : form,
        'clients'        : clients,
        'enquiry_form'   : enquiry_form,
        'enquiry_clients': enquiry_clients,
        'success_message': success_message,
        'error_message'  : error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/client_add.html', context)


@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def enquiry_client_add(request):
    """  Add new enquiry and see the list of clients """
    success_message, error_message = None, None
    form    = ClientForm
    clients = Client.objects.all()
    enquiry_form    = EnquiryClientForm
    enquiry_clients = EnquiryClient.objects.all()
    
    if request.method=="POST":
        enquiry_form = EnquiryClientForm(request.POST, request.FILES)
        if enquiry_form.is_valid():
            obj            = enquiry_form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            obj.save()
            success_message = "added a new enquiry client"
        else:
            error_message = "to add a new enquiry client"
            
    context = {
        'form': form,
        'enquiry_form': enquiry_form,
        'clients': clients,
        'enquiry_clients': enquiry_clients,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/client_add.html', context)


@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def enquiry_client_details(request,id):
    """  view and update a enquiry client depending on id """
    success_message, error_message = None, None  
    enquiry_client = get_object_or_404(EnquiryClient, id=id)
    enquiry_form = EnquiryClientForm(instance=enquiry_client)  
    
    if request.method=="POST":
        enquiry_form = EnquiryClientForm(request.POST, instance=enquiry_client)
        if enquiry_form.is_valid():
            enquiry_form.save()
            success_message = "updated enquiry client"
        else:
            error_message = "to update enquiry client"
            
    context = {
        'enquiry_form': enquiry_form,
        'enquiry_client': enquiry_client,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/enquiry_client_details.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def enquiry_client_delete(request,id):
    """  delete a specific enquiry client depending on id """
    success_message, error_message = None, None
    form            = ClientForm()    
    enquiry_client  = get_object_or_404(EnquiryClient, id=id)
    clients         = Client.objects.all()
    enquiry_form    = EnquiryClientForm
    enquiry_clients = EnquiryClient.objects.all()
    
    if request.method=="POST":
        enquiry_client.delete()
        success_message = "deleted enquiry client"
    else:
        error_message = "to delete enquiry client"
        
    context = {
        'form': form,
        'clients': clients,
        'enquiry_form': enquiry_form,
        'enquiry_clients': enquiry_clients,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/client_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])   
def air_port_add(request):
    """  Add new air_port and see the list of air_ports packages """
    success_message, error_message = None, None
    form = AirPortForm
    air_ports = AirPort.objects.all()
    
    if request.method=="POST":
        form = AirPortForm(request.POST)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            obj.save()
            success_message = "added a new air port"
        else:
            error_message = "to add a new air port"
            
    context = {
        'form': form,
        'air_ports': air_ports,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/air_port_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def air_port_details(request,id):
    """  view and update a air_port depending on id """
    success_message, error_message = None, None  
    air_port = get_object_or_404(AirPort, id=id)
    form = AirPortForm(instance=air_port)  
    
    if request.method=="POST":
        form = AirPortForm(request.POST, instance=air_port)
        if form.is_valid():
            form.save()
            success_message = "updated air port"
        else:
            error_message = "to update air port"
            
    context = {
        'form': form,
        'air_port': air_port,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/air_port_details.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['admin'])
def air_port_delete(request,id):
    """  delete a specific air_port depending on id """
    success_message, error_message = None, None
    form = AirPortForm()    
    air_port = get_object_or_404(AirPort, id=id)
    air_ports = AirPortt.objects.all()
    
    if request.method=="POST":
        air_port.delete()
        success_message = "deleted air port"
    else:
        error_message = "to delete air port"
        
    context = {
        'form': form,
        'air_ports': air_ports,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'admin/air_port_add.html', context)
    

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])   
def air_ticket_add(request):
    """  Add new air_ticket and see the list of air_ticket packages """
    success_message, error_message = None, None
    form = AirTicketForm
    air_tickets = AirTicket.objects.all()
    
    if request.method=="POST":
        form = AirTicketForm(request.POST)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            obj.save()
            success_message = "added a new air ticket"
        else:
            error_message = "to add a new air ticket"
            
    context = {
        'form': form,
        'air_tickets': air_tickets,
        'air_ports': AirPort.objects.all(),
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/air_ticket_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def air_ticket_details(request,id):
    """  view and update a air_ticket depending on id """
    success_message, error_message = None, None  
    air_ticket = get_object_or_404(AirTicket, id=id)
    form = AirTicketForm(instance=air_ticket)  
    
    if request.method=="POST":
        form = AirTicketForm(request.POST, instance=air_ticket)
        if form.is_valid():
            form.save()
            success_message = "updated air ticket"
        else:
            error_message = "to update air ticket"
            
    context = {
        'form': form,
        'air_ticket': air_ticket,
        'air_ports': AirPort.objects.all(),
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/air_ticket_details.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def air_ticket_delete(request,id):
    """  delete a specific air_ticket depending on id """
    success_message, error_message = None, None
    form = AirTicketForm()    
    air_ticket = get_object_or_404(AirTicket, id=id)
    air_tickets = AirTicket.objects.all()
    
    if request.method=="POST":
        air_ticket.delete()
        success_message = "deleted air ticket"
    else:
        error_message = "to delete air ticket"
        
    context = {
        'form': form,
        'air_tickets': air_tickets,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/air_ticket_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def islamic_add(request):
    """  Add new package and see the list of packages """
    success_message, error_message = None, None
    form = IslamicForm    
    islamics = Islamic.objects.all()
    
    if request.method=="POST":
        form = IslamicForm(request.POST)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            obj.save()
            success_message = "added a new islamic"
        else:
            error_message = "to add a new islamic"
            
    context = {
        'form': form,
        'islamics': islamics,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/islamic_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def islamic_details(request,id):
    """  view and update a islamic depending on id """
    success_message, error_message = None, None  
    islamic = get_object_or_404(Islamic, id=id)
    form = IslamicForm(instance=islamic)  
    
    if request.method=="POST":
        form = IslamicForm(request.POST, instance=islamic)
        if form.is_valid():
            form.save()
            success_message = "updated islamic package"
        else:
            error_message = "to update islamic package"
            
    context = {
        'form': form,
        'islamic': islamic,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/islamic_details.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def islamic_delete(request,id):
    """  delete a specific islamic depending on id """
    success_message, error_message = None, None
    form = IslamicForm()    
    islamic = get_object_or_404(Islamic, id=id)
    islamics = Islamic.objects.all()
    
    if request.method=="POST":
        islamic.delete()
        success_message = "deleted islamic package"
    else:
        error_message = "to delete islamic package"
        
    context = {
        'form': form,
        'islamics': islamics,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/islamic_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def tour_add(request):
    """  Add new tour and see the list of tour packages """
    success_message, error_message = None, None
    form = TourForm        
    tours = Tour.objects.all()
    
    if request.method=="POST":
        form = TourForm(request.POST)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            obj.save()
            success_message = "added a new vistoura"
        else:
            error_message = "to add a new tour"
            
    context = {
        'form': form,
        'tours': tours,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/tour_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def tour_details(request,id):
    """  view and update tour depending on id """
    success_message, error_message = None, None  
    tour = get_object_or_404(Tour, id=id)
    form = TourForm(instance=tour)  
    
    if request.method=="POST":
        form = TourForm(request.POST, instance=tour)
        if form.is_valid():
            form.save()
            success_message = "updated tour"
        else:
            error_message = "to update tour"
            
    context = {
        'form': form,
        'tour': tour,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/tour_details.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def tour_delete(request,id):
    """  delete tour depending on id """
    success_message, error_message = None, None
    form = TourForm()    
    tour = get_object_or_404(Tour, id=id)
    tours = Tour.objects.all()
    
    if request.method=="POST":
        tour.delete()
        success_message = "deleted tour"
    else:
        error_message = "to delete tour"
        
    context = {
        'form': form,
        'tours': tours,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/tour_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def visa_add(request):
    """  Add new visa and see the list of visa packages """
    success_message, error_message = None, None            
    form = VisaForm   
    visas = Visa.objects.all()
    
    if request.method=="POST":
        form = VisaForm(request.POST)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            obj.save()
            success_message = "added a new visa"
        else:
            error_message = "to add a new visa"
            
    context = {
        'form': form,
        'visas': visas,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/visa_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def visa_details(request,id):
    """  view and update a visa depending on id """
    success_message, error_message = None, None  
    visa = get_object_or_404(Visa, id=id)
    form = VisaForm(instance=visa)  
    
    if request.method=="POST":
        form = VisaForm(request.POST, instance=visa)
        if form.is_valid():
            form.save()
            success_message = "updated visa"
        else:
            error_message = "to update visa"
            
    context = {
        'form': form,
        'visa': visa,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/visa_details.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def visa_delete(request,id):
    """  delete a specific visa depending on id """
    success_message, error_message = None, None
    form = VisaForm()    
    visa = get_object_or_404(Visa, id=id)
    visas = Visa.objects.all()
    
    if request.method=="POST":
        visa.delete()
        success_message = "deleted visa"
    else:
        error_message = "to delete visa"
        
    context = {
        'form': form,
        'visas': visas,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/visa_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])   
def package_tour(request):
    """  creating tour package for customer """
    tours = Tour.objects.all()[::-1]
    package_tours = PackageTour.objects.all()[::-1]
    
    context = {
        'tours': tours,
        'package_tours': package_tours,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_tour.html', context)
  
  
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_tour_add(request,id):
    """  creating tour package for customer """
    success_message, error_message = None, None
    tour = get_object_or_404(Tour, id=id)    
    form = PackageTourForm(instance=tour)
    
    if request.method=="POST":
        form = PackageTourForm(request.POST)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            # if the package is for enquiry it will not add to cart
            if obj.client.name != 'Enquiry Client':
                print(obj.client.name)
                obj.in_cart    = True
            obj.save()
            # adding the package into cart
            if obj.in_cart == True:
                cart = Cart(created_by=obj.created_by, package_tour=obj)
                cart.save()
            success_message = "added a new tour"
        else:
            error_message = "to add a new tour"
            
    context = {
        'form': form,
        'tour': tour,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_tour_add.html', context)
  
  
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_tour_details(request,id):
    """  updating tour package for customer """
    success_message, error_message = None, None
    package_tour = get_object_or_404(PackageTour, id=id)    
    form         = PackageTourForm(instance=package_tour)
    
    if request.method=="POST":
        form = PackageTourForm(request.POST, instance=package_tour)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            # if the package is for enquiry it will not add to cart
            if obj.client.name != 'Enquiry Client':
                print(obj.client.name)
                obj.in_cart    = True
            obj.save()
            # adding the package into cart
            if obj.in_cart == True:
                cart = Cart(created_by=obj.created_by, package_tour=obj)
                cart.save()
            success_message = "updated a tour"
        else:
            error_message = "to update a tour"
            
    context = {
        'form': form,
        'tour': package_tour,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_tour_details.html', context)
    
    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_tour_delete(request,id):
    """  delete tour package for customer """
    success_message, error_message = None, None
    package_tour  = get_object_or_404(PackageTour, id=id)   
    tours         = Tour.objects.all()   
    package_tours = PackageTour.objects.all()   
    
    if request.method=="POST":
        package_tour.delete()
        success_message = "deleted a tour"
    else:
        error_message = "to delete a tour"
            
    context = {
        'tours': tours,
        'package_tours': package_tours,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_tour.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_islamic(request):
    """  view islamic package for customer """
    islamics = Islamic.objects.all()[::-1]
    package_islamics = PackageIslamic.objects.all()[::-1]
    
    context = {
        'islamics': islamics,
        'package_islamics': package_islamics,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_islamic.html', context)
    
    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_islamic_add(request,id):
    """  creating islamic package for customer """
    success_message, error_message = None, None
    islamic = get_object_or_404(Islamic, id=id)    
    form = PackageIslamicForm(instance=islamic)
    
    if request.method=="POST":
        form = PackageIslamicForm(request.POST)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            # if the package is for enquiry it will not add to cart
            if obj.client.name != 'Enquiry Client':
                print(obj.client.name)
                obj.in_cart    = True
            obj.save()
            # adding the package into cart
            if obj.in_cart == True:
                cart = Cart(created_by=obj.created_by, package_islamic=obj)
                cart.save()
            success_message = "added a new islamic package"
        else:
            error_message = "to add a new islamic package"
            
    context = {
        'form': form,
        'islamic': islamic,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_islamic_add.html', context)
    
    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_islamic_details(request,id):
    """  updating islamic package for customer """
    success_message, error_message = None, None
    package_islamic = get_object_or_404(PackageIslamic, id=id)    
    form            = PackageIslamicForm(instance=package_islamic)
    
    if request.method=="POST":
        form = PackageIslamicForm(request.POST, instance=package_islamic)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            # if the package is for enquiry it will not add to cart
            if obj.client.name != 'Enquiry Client':
                print(obj.client.name)
                obj.in_cart    = True
            obj.save()
            # adding the package into cart
            if obj.in_cart == True:
                cart = Cart(created_by=obj.created_by, package_islamic=obj)
                cart.save()
            success_message = "updated a islamic package"
        else:
            error_message = "to update a islamic package"
            
    context = {
        'form': form,
        'islamic': package_islamic,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_islamic_details.html', context)
    
    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_islamic_delete(request,id):
    """  delete islamic package for customer """
    success_message, error_message = None, None
    package_islamic  = get_object_or_404(PackageIslamic, id=id)   
    islamics         = Islamic.objects.all()   
    package_islamics = PackageIslamic.objects.all()   
    
    if request.method=="POST":
        package_islamic.delete()
        success_message = "deleted a islamic package"
    else:
        error_message = "to delete a islamic package"
            
    context = {
        'islamics': islamics,
        'package_islamics': package_islamics,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_islamic.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_air_ticket(request):
    """  view air ticket package for customer """
    air_tickets = AirTicket.objects.all()[::-1]
    package_air_tickets = PackageAirTicket.objects.all()[::-1]
    
    context = {
        'air_tickets': air_tickets,
        'package_air_tickets': package_air_tickets,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_air_ticket.html', context)
    

@login_required(login_url='login')
@has_access(allowed_roles=['employee'])   
def package_air_ticket_add(request,id):
    """  creating air_ ticket package for customer """
    success_message, error_message = None, None
    air_ticket = get_object_or_404(AirTicket, id=id)    
    form = PackageAirTicketForm(instance=air_ticket)
    
    if request.method=="POST":
        form = PackageAirTicketForm(request.POST)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            # if the package is for enquiry it will not add to cart
            if obj.client.name != 'Enquiry Client':
                print(obj.client.name)
                obj.in_cart    = True
            obj.save()
            # adding the package into cart
            if obj.in_cart == True:
                cart = Cart(created_by=obj.created_by, package_air_ticket=obj)
                cart.save()
            success_message = "added a new air ticket"
        else:
            error_message = "to add a new air ticket"
            
    context = {
        'form': form,
        'air_ticket': air_ticket,
        'air_ports': AirPort.objects.all(),
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_air_ticket_add.html', context)
 
 
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])   
def package_air_ticket_details(request,id):
    """  updating air ticket for customer """
    success_message, error_message = None, None
    package_air_ticket = get_object_or_404(PackageAirTicket, id=id)    
    form         = PackageAirTicketForm(instance=package_air_ticket)
    
    if request.method=="POST":
        form = PackageAirTicketForm(request.POST, instance=package_air_ticket)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            # if the package is for enquiry it will not add to cart
            if obj.client.name != 'Enquiry Client':
                print(obj.client.name)
                obj.in_cart    = True
            obj.save()
            # adding the package into cart
            if obj.in_cart == True:
                cart = Cart(created_by=obj.created_by, package_air_ticket=obj)
                cart.save()
            success_message = "updated a air ticket"
        else:
            error_message = "to update a air ticket"
            
    context = {
        'form': form,
        'air_ticket': package_air_ticket,
        'air_ports': AirPort.objects.all(),
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_air_ticket_details.html', context)
  
  
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_air_ticket_delete(request,id):
    """  delete air ticket for customer """
    success_message, error_message = None, None
    package_air_ticket  = get_object_or_404(PackageAirTicket, id=id)   
    air_tickets         = AirTicket.objects.all()   
    package_air_tickets = PackageAirTicket.objects.all()   
    
    if request.method=="POST":
        package_air_ticket.delete()
        success_message = "deleted a air ticket"
    else:
        error_message = "to delete a air ticket"
            
    context = {
        'air_tickets': air_tickets,
        'package_air_tickets': package_air_tickets,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_air_ticket.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_visa(request):
    """  view visa package for customer """
    visas = Visa.objects.all()[::-1]
    package_visas = PackageVisa.objects.all()[::-1]
    
    context = {
        'visas': visas,
        'package_visas': package_visas,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_visa.html', context)
 
 
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_visa_add(request,id):
    """  creating visa package for customer """
    success_message, error_message = None, None
    visa = get_object_or_404(Visa, id=id)    
    form = PackageVisaForm(instance=visa)
    
    if request.method=="POST":
        form = PackageVisaForm(request.POST)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            # if the package is for enquiry it will not add to cart
            if obj.client.name != 'Enquiry Client':
                print(obj.client.name)
                obj.in_cart    = True
            obj.save()
            # adding the package into cart
            if obj.in_cart == True:
                cart = Cart(created_by=obj.created_by, package_visa=obj)
                cart.save()
            success_message = "added a new visa package"
        else:
            error_message = "to add a new visa package"
            
    context = {
        'form': form,
        'visa': visa,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_visa_add.html', context)
    
    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])   
def package_visa_details(request,id):
    """  updating visa package for customer """
    success_message, error_message = None, None
    package_visa = get_object_or_404(PackageVisa, id=id)    
    form         = PackageVisaForm(instance=package_visa)
    
    if request.method=="POST":
        form = PackageVisaForm(request.POST, instance=package_visa)
        if form.is_valid():
            obj            = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
            # if the package is for enquiry it will not add to cart
            if obj.client.name != 'Enquiry Client':
                print(obj.client.name)
                obj.in_cart    = True
            obj.save()
            # adding the package into cart
            if obj.in_cart == True:
                cart = Cart(created_by=obj.created_by, package_visa=obj)
                cart.save()
            success_message = "updated a visa package"
        else:
            error_message = "to update a visa package"
            
    context = {
        'form': form,
        'visa': package_visa,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_visa_details.html', context)
   
   
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def package_visa_delete(request,id):
    """  delete visa package for customer """
    success_message, error_message = None, None
    package_visa  = get_object_or_404(PackageVisa, id=id)   
    visas         = Visa.objects.all()   
    package_visas = PackageVisa.objects.all()   
    
    if request.method=="POST":
        package_visa.delete()
        success_message = "deleted a visa package"
    else:
        error_message = "to delete a visa package"
            
    context = {
        'visas': visas,
        'package_visas': package_visas,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/package_visa.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def client_marketing(request):
    clients = Client.objects.all()
    
    context = {
        'clients': clients,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/marketing.html', context)
    
    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def payment(request): 
    """ all packages along with payment info and seperate due list """       
    orders = Order.objects.all()[::-1]
    
    context = {
        'orders'       : orders,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/payment.html', context)  
    
    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def payment_details(request, id): 
    """ Payment details """    
    success_message, error_message = None, None
    order = Order.objects.get(id=id)
    form = OrderForm(instance=order)  
    
    if request.method=="POST":
        form = OrderForm(request.POST, request.FILES, instance=order) 
        if form.is_valid():
            form.save()
            
            success_message = "updated payment details"
        else:
            error_message = "to update payment details"
            
    context = {
        'order'    : order,
        'form'     : form,
        'success_message': success_message,
        'error_message':error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/payment_details.html', context)   
    
   
    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])    
def request_custom_package(request): 
    """ all packages along with payment info and seperate due list """       
    tours               = Tour.objects.filter(created_by__employee_id=request.user.username)[::-1]
    islamics            = Islamic.objects.filter(created_by__employee_id=request.user.username)[::-1]
    air_tickets         = AirTicket.objects.filter(created_by__employee_id=request.user.username)[::-1]
    visas               = Visa.objects.filter(created_by__employee_id=request.user.username)[::-1]
    package_tours       = PackageTour.objects.filter(created_by__employee_id=request.user.username)[::-1]
    package_islamics    = PackageIslamic.objects.filter(created_by__employee_id=request.user.username)[::-1]
    package_air_tickets = PackageAirTicket.objects.filter(created_by__employee_id=request.user.username)[::-1]
    package_visas       = PackageVisa.objects.filter(created_by__employee_id=request.user.username)[::-1]
    
    context = {
        'tours'               : tours,
        'islamics'            : islamics,
        'air_tickets'         : air_tickets,
        'visas'               : visas,
        'package_tours'       : package_tours,
        'package_islamics'    : package_islamics,
        'package_air_tickets' : package_air_tickets,
        'package_visas'       : package_visas,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/request_custom_package.html', context)     
    

@login_required(login_url='login')
@has_access(allowed_roles=['employee'])      
def cart_details(request):
    """ cart will temporary store the packages for order """
    carts = Cart.objects.filter(created_by__employee_id=request.user.username)
    message, client_info,  client_id, form = None, None, None, None
    total_ammount = 0
    
    if carts.count() != 0:
        print(carts)
        for cart in carts:        
            if cart.package_tour:
                client_id = cart.package_tour.client.id
                total_ammount += cart.package_tour.client_price
            elif cart.package_islamic:
                client_id = cart.package_islamic.client.id
                total_ammount += cart.package_islamic.client_price
            elif cart.package_air_ticket:
                client_id = cart.package_air_ticket.client.id
                total_ammount += cart.package_air_ticket.client_price
            elif cart.package_visa:
                client_id = cart.package_visa.client.id
                total_ammount += cart.package_visa.client_price
                
        
        data = {
                'total_ammount': total_ammount,
               }
                       
        form = OrderForm(initial=data)            
        client_info = Client.objects.get(id=client_id)
        
    else:
        message = "No Item Found."
        
    context = {
        'message': message,
        'form': form,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'client_info': client_info,
        'cart': carts.count,
        'carts': carts,
    }
    return render(request, 'employee/cart.html', context)    



@login_required(login_url='login')
@has_access(allowed_roles=['employee'])      
def cart_delete(request, id):
    """ delete an item/package from cart before making an order """
    cart_item = Cart.objects.get(id=id)
    cart_item.delete()
    
    return redirect('/e/cart/details') 
    

@login_required(login_url='login')
@has_access(allowed_roles=['employee'])      
def order(request):
    """
      4 major task
        - Adding all cart item of a specific client into Order table
        - Deleting the carts item
        - Make a pdf and send a mail of invoice
        - Print invoice     
    """ 
    client_id, actual_price = None, 0
    orders = Order.objects.all()[::-1]
    carts = Cart.objects.filter(created_by__employee_id=request.user.username)  
    
    # adding items into order and deleteing from cart
    if request.method == "POST":
        # adding
        form = OrderForm(request.POST, request.FILES)  
        if form.is_valid():
            obj = form.save(commit=False)
            obj.created_by = Employee.objects.get(employee_id=request.user.username)
                  
            for cart in carts:        
                if cart.package_tour:
                    client_id = cart.package_tour.client.id
                    actual_price += cart.package_tour.actual_price
                    obj.package_tour = PackageTour.objects.get(id=cart.package_tour.id)
                elif cart.package_islamic:
                    client_id = cart.package_islamic.client.id
                    actual_price += cart.package_islamic.actual_price
                    obj.package_islamic = PackageIslamic.objects.get(id=cart.package_islamic.id)
                elif cart.package_air_ticket:
                    client_id = cart.package_air_ticket.client.id
                    actual_price += cart.package_air_ticket.actual_price
                    obj.package_air_ticket = PackageAirTicket.objects.get(id=cart.package_air_ticket.id)
                elif cart.package_visa:
                    client_id = cart.package_visa.client.id
                    actual_price += cart.package_visa.actual_price
                    obj.package_visa = PackageVisa.objects.get(id=cart.package_visa.id)
            obj.actual_price = actual_price
            obj.client = Client.objects.get(id=client_id)
            obj.save()
            
            # deleting
            carts.delete()
            
            
    context = {
        'form'     : form,
        'orders'   : orders,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart'     : Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/payment.html', context)   

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])      
def invoice(request):
    last_order = Order.objects.filter(created_by__employee_id=request.user.username).last()
    
    context = {
        'order': last_order,
    }
    return render(request, 'employee/invoice.html', context)      

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])      
def specific_invoice(request, id):
    order = Order.objects.get(id=id)
    
    context = {
        'order': order,
    }
    return render(request, 'employee/invoice.html', context)    

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def expenditure_add(request):
    """  Add new expenditure and see the list of expenditure """
    success_message, error_message = None, None            
    form = ExpenditureForm   
    expenditures = Expenditure.objects.all()[::-1]
    
    if request.method=="POST":
        form = ExpenditureForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "added a new expenditure"
        else:
            error_message = "to add a new expenditure"
            
    context = {
        'form': form,
        'expenditures': expenditures,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/expenditure_add.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def expenditure_details(request,id):
    """  view and update a expenditure depending on id """
    success_message, error_message = None, None  
    expenditure = get_object_or_404(Expenditure, id=id)
    form = ExpenditureForm(instance=expenditure)  
    
    if request.method=="POST":
        form = ExpenditureForm(request.POST, instance=expenditure)
        if form.is_valid():
            form.save()
            success_message = "updated expenditure"
        else:
            error_message = "to update expenditure"
            
    context = {
        'form': form,
        'expenditure': expenditure,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/expenditure_details.html', context)

    
@login_required(login_url='login')
@has_access(allowed_roles=['employee'])
def expenditure_delete(request,id):
    """  delete a specific expenditure depending on id """
    success_message, error_message = None, None
    form = ExpenditureForm()    
    expenditure = get_object_or_404(Expenditure, id=id)
    expenditures = Expenditure.objects.all()
    
    if request.method=="POST":
        expenditure.delete()
        success_message = "deleted expenditure"
    else:
        error_message = "to delete expenditure"
        
    context = {
        'form': form,
        'expenditures': expenditures,
        'success_message': success_message,
        'error_message': error_message,
        'user_info': Employee.objects.get(employee_id=request.user.username),
        'cart': Cart.objects.filter(created_by__employee_id=request.user.username).count,
    }
    return render(request, 'employee/expenditure_add.html', context)
    
    
    
    
    
    
    
    
    
    
    
    
    