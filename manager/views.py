from django.shortcuts import get_object_or_404, render
from .forms import (  ClientForm, EnquiryClientForm, AirTicketForm, 
                      IslamicForm, TourForm, VisaForm, 
                      PackageTourForm, PackageIslamicForm,
                      PackageAirTicketForm, PackageVisaForm,
                   )
from .models import ( Client, EnquiryClient, AirTicket, 
                      Islamic, Tour, Visa, 
                      PackageTour, PackageIslamic,
                      PackageAirTicket, PackageVisa,
                    )


def index(request):
    """  Manager's Dashboard """
    earning_overview = [0, 10000, 5000, 15000, 10000, 20000, 15000, 25000, 20000, 30000, 25000, 40000]
    clients        = Client.objects.all()
    
    context = {
        'earning_overview': earning_overview,
        'clients': clients,
        'total_packages': package_count(),
    }
    return render(request, 'manager/index.html', context)

    
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
    print(count)
    return count
    

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
            form.save()
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
    }
    return render(request, 'manager/client_add.html', context)


def client_details(request,id):
    """  view and update a client depending on id """
    success_message, error_message = None, None  
    client = get_object_or_404(Client, id=id)
    form   = ClientForm(instance=client)
    # All packages taken by a specific user    
    package_tours       = PackageTour.objects.filter(id=id)
    package_islamics    = PackageIslamic.objects.filter(id=id)
    package_air_tickets = PackageAirTicket.objects.filter(id=id)
    package_visas       = PackageVisa.objects.filter(id=id)
    
    if request.method=="POST":
        form = ClientForm(request.POST, instance=client)
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
    }
    return render(request, 'manager/client_details.html', context)


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
    }
    return render(request, 'manager/client_add.html', context)


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
            enquiry_form.save()
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
    }
    return render(request, 'manager/client_add.html', context)


def enquiry_client_details(request,id):
    """  view and update a enquiry client depending on id """
    success_message, error_message = None, None  
    enquiry_client = get_object_or_404(EnquiryClient, id=id)
    enquiry_form = EnquiryClientForm(instance=enquiry_client)  
    
    if request.method=="POST":
        form = EnquiryClientForm(request.POST, instance=enquiry_client)
        if enquiry_form.is_valid():
            enquiry_form.save()
            success_message = "updated enquiry client"
        else:
            error_message = "to update enquiry client"
            
    context = {
        'enquiry_form': form,
        'enquiry_client': enquiry_client,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/enquiry_client_details.html', context)


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
    }
    return render(request, 'manager/client_add.html', context)

    
def air_ticket_add(request):
    """  Add new air_ticket and see the list of air_ticket packages """
    success_message, error_message = None, None
    form = AirTicketForm
    air_tickets = AirTicket.objects.all()
    
    if request.method=="POST":
        form = AirTicketForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "added a new air ticket"
        else:
            error_message = "to add a new air ticket"
            
    context = {
        'form': form,
        'air_tickets': air_tickets,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/air_ticket_add.html', context)


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
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/air_ticket_details.html', context)


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
    }
    return render(request, 'manager/air_ticket_add.html', context)


def islamic_add(request):
    """  Add new package and see the list of packages """
    success_message, error_message = None, None
    form = IslamicForm    
    islamics = Islamic.objects.all()
    
    if request.method=="POST":
        form = IslamicForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "added a new islamic"
        else:
            error_message = "to add a new islamic"
            
    context = {
        'form': form,
        'islamics': islamics,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/islamic_add.html', context)


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
    }
    return render(request, 'manager/islamic_details.html', context)


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
    }
    return render(request, 'manager/islamic_add.html', context)


def tour_add(request):
    """  Add new tour and see the list of tour packages """
    success_message, error_message = None, None
    form = TourForm        
    tours = Tour.objects.all()
    
    if request.method=="POST":
        form = TourForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "added a new vistoura"
        else:
            error_message = "to add a new tour"
            
    context = {
        'form': form,
        'tours': tours,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/tour_add.html', context)


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
    }
    return render(request, 'manager/tour_details.html', context)


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
    }
    return render(request, 'manager/tour_add.html', context)


def visa_add(request):
    """  Add new visa and see the list of visa packages """
    success_message, error_message = None, None            
    form = VisaForm   
    visas = Visa.objects.all()
    
    if request.method=="POST":
        form = VisaForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "added a new visa"
        else:
            error_message = "to add a new visa"
            
    context = {
        'form': form,
        'visas': visas,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/visa_add.html', context)


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
    }
    return render(request, 'manager/visa_details.html', context)


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
    }
    return render(request, 'manager/visa_add.html', context)

    
def package_tour(request):
    """  creating tour package for customer """
    tours = Tour.objects.all()
    package_tours = PackageTour.objects.all()
    
    context = {
        'tours': tours,
        'package_tours': package_tours,
    }
    return render(request, 'manager/package_tour.html', context)
    
    
def package_tour_add(request,id):
    """  creating tour package for customer """
    success_message, error_message = None, None
    tour = get_object_or_404(Tour, id=id)    
    form = PackageTourForm(instance=tour)
    
    if request.method=="POST":
        form = PackageTourForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "added a new tour"
        else:
            error_message = "to add a new tour"
            
    context = {
        'form': form,
        'tour': tour,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/package_tour_add.html', context)
    
    
def package_tour_details(request,id):
    """  updating tour package for customer """
    success_message, error_message = None, None
    package_tour = get_object_or_404(PackageTour, id=id)    
    form         = PackageTourForm(instance=package_tour)
    
    if request.method=="POST":
        form = PackageTourForm(request.POST, instance=package_tour)
        if form.is_valid():
            form.save()
            success_message = "updated a tour"
        else:
            error_message = "to update a tour"
            
    context = {
        'form': form,
        'tour': package_tour,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/package_tour_details.html', context)
    
    
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
    }
    return render(request, 'manager/package_tour.html', context)

    
def package_islamic(request):
    """  view islamic package for customer """
    islamics = Islamic.objects.all()
    package_islamics = PackageIslamic.objects.all()
    
    context = {
        'islamics': islamics,
        'package_islamics': package_islamics,
    }
    return render(request, 'manager/package_islamic.html', context)
    
    
def package_islamic_add(request,id):
    """  creating islamic package for customer """
    success_message, error_message = None, None
    islamic = get_object_or_404(Islamic, id=id)    
    form = PackageIslamicForm(instance=islamic)
    
    if request.method=="POST":
        form = PackageIslamicForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "added a new islamic package"
        else:
            error_message = "to add a new islamic package"
            
    context = {
        'form': form,
        'islamic': islamic,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/package_islamic_add.html', context)
    
    
def package_islamic_details(request,id):
    """  updating islamic package for customer """
    success_message, error_message = None, None
    package_islamic = get_object_or_404(PackageIslamic, id=id)    
    form            = PackageIslamicForm(instance=package_islamic)
    
    if request.method=="POST":
        form = PackageIslamicForm(request.POST, instance=package_islamic)
        if form.is_valid():
            form.save()
            success_message = "updated a islamic package"
        else:
            error_message = "to update a islamic package"
            
    context = {
        'form': form,
        'islamic': package_islamic,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/package_islamic_details.html', context)
    
    
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
    }
    return render(request, 'manager/package_islamic.html', context)

    
def package_air_ticket(request):
    """  view air ticket package for customer """
    air_tickets = AirTicket.objects.all()
    package_air_tickets = PackageAirTicket.objects.all()
    
    context = {
        'air_tickets': air_tickets,
        'package_air_tickets': package_air_tickets,
    }
    return render(request, 'manager/package_air_ticket.html', context)
    
    
def package_air_ticket_add(request,id):
    """  creating air_ ticket package for customer """
    success_message, error_message = None, None
    air_ticket = get_object_or_404(AirTicket, id=id)    
    form = PackageAirTicketForm(instance=air_ticket)
    
    if request.method=="POST":
        form = PackageAirTicketForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "added a new air ticket"
        else:
            error_message = "to add a new air ticket"
            
    context = {
        'form': form,
        'air_ticket': air_ticket,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/package_air_ticket_add.html', context)
    
    
def package_air_ticket_details(request,id):
    """  updating air ticket for customer """
    success_message, error_message = None, None
    package_air_ticket = get_object_or_404(PackageAirTicket, id=id)    
    form         = PackageAirTicketForm(instance=package_air_ticket)
    
    if request.method=="POST":
        form = PackageAirTicketForm(request.POST, instance=package_air_ticket)
        if form.is_valid():
            form.save()
            success_message = "updated a air ticket"
        else:
            error_message = "to update a air ticket"
            
    context = {
        'form': form,
        'air_ticket': package_air_ticket,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/package_air_ticket_details.html', context)
    
    
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
    }
    return render(request, 'manager/package_air_ticket.html', context)

    
def package_visa(request):
    """  view visa package for customer """
    visas = Visa.objects.all()
    package_visas = PackageVisa.objects.all()
    
    context = {
        'visas': visas,
        'package_visas': package_visas,
    }
    return render(request, 'manager/package_visa.html', context)
    
    
def package_visa_add(request,id):
    """  creating visa package for customer """
    success_message, error_message = None, None
    visa = get_object_or_404(Visa, id=id)    
    form = PackageVisaForm(instance=visa)
    
    if request.method=="POST":
        form = PackageVisaForm(request.POST)
        if form.is_valid():
            form.save()
            success_message = "added a new visa package"
        else:
            error_message = "to add a new visa package"
            
    context = {
        'form': form,
        'visa': visa,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/package_visa_add.html', context)
    
    
def package_visa_details(request,id):
    """  updating visa package for customer """
    success_message, error_message = None, None
    package_visa = get_object_or_404(PackageVisa, id=id)    
    form         = PackageVisaForm(instance=package_visa)
    
    if request.method=="POST":
        form = PackageVisaForm(request.POST, instance=package_visa)
        if form.is_valid():
            form.save()
            success_message = "updated a visa package"
        else:
            error_message = "to update a visa package"
            
    context = {
        'form': form,
        'visa': package_visa,
        'success_message': success_message,
        'error_message': error_message,
    }
    return render(request, 'manager/package_visa_details.html', context)
    
    
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
    }
    return render(request, 'manager/package_visa.html', context)


def client_marketing(request):
    clients = Client.objects.all()
    
    context = {
        'clients': clients,
    }
    return render(request, 'manager/marketing.html', context)

    
def payment(request): 
    """ all packages along with payment info and seperate due list """       
    package_tours       = PackageTour.objects.all()
    package_islamics    = PackageIslamic.objects.all()
    package_air_tickets = PackageAirTicket.objects.all()
    package_visas       = PackageVisa.objects.all()
    
    context = {
        'package_tours'       : package_tours,
        'package_islamics'    : package_islamics,
        'package_air_tickets' : package_air_tickets,
        'package_visas'       : package_visas,
    }
    return render(request, 'manager/payment.html', context)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    