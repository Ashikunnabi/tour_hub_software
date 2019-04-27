from django.db import models


class Client(models.Model):
    BLOOD_GROUP = (
        ('1', 'A+'), ('2', 'B+'), ('3', 'O+'), ('4', 'AB+'),
        ('5', 'A-'), ('6', 'B-'), ('7', 'O-'), ('8', 'AB-'),
    ) 
    name                 = models.CharField(max_length=50)
    phone                = models.IntegerField()
    email                = models.EmailField()
    nid                  = models.IntegerField()
    profession           = models.CharField(max_length=50)
    blood_group          = models.CharField(max_length=1, choices=BLOOD_GROUP, default=1)
    present_address      = models.CharField(max_length=200)
    permanent_address    = models.CharField(max_length=200)
    photo                = models.FileField()
    
    def __str__(self):
        return self.name


class EnquiryClient(models.Model):
    BLOOD_GROUP = (
        ('1', 'A+'), ('2', 'B+'), ('3', 'O+'), ('4', 'AB+'),
        ('5', 'A-'), ('6', 'B-'), ('7', 'O-'), ('8', 'AB-'),
    ) 
    TOUR_TYPE = (
        ('1', 'Normal Tour'),
        ('2', 'Oficial Tour'),
        ('3', 'Honeymoon'),
        ('4', 'Hajj'),
        ('5', 'Umrah'),
        ('6', 'Air Ticket'),
        ('7', 'Visa Processing'),
    )
    name              = models.CharField(max_length=50)
    phone             = models.IntegerField()
    email             = models.EmailField()
    nid               = models.IntegerField()
    profession        = models.CharField(max_length=50)
    blood_group       = models.CharField(max_length=1, choices=BLOOD_GROUP, default=1)
    present_address   = models.CharField(max_length=200)
    permanent_address = models.CharField(max_length=200)
    photo             = models.FileField()
    type              = models.CharField(max_length=1, choices=TOUR_TYPE, blank=True, null=True)
    country_name      = models.CharField(max_length=30, blank=True, null=True)
    places            = models.CharField(max_length=200, blank=True, null=True)
    members           = models.IntegerField(blank=True, null=True)
    airline           = models.CharField(max_length=100, blank=True, null=True)
    duration          = models.CharField(max_length=30, blank=True, null=True)
    client_price      = models.IntegerField(blank=True, null=True)  
    
    
    def __str__(self):
        return self.name


class AirTicket(models.Model):
    airline        = models.CharField(max_length=100)
    departure_from = models.CharField(max_length=100)
    departure_to   = models.CharField(max_length=100)
    actual_price   = models.IntegerField()
    client_price   = models.IntegerField()


class Islamic(models.Model):
    TOUR_TYPE = (
        ('1', 'Hazz'),
        ('2', 'Umrah'),
    )
    title    = models.CharField(max_length=30)
    type     = models.CharField(max_length=1, choices=TOUR_TYPE, default=1)
    places   = models.CharField(max_length=200)
    duration_days   = models.CharField(max_length=3)
    duration_nights = models.CharField(max_length=3)
    members         = models.IntegerField()
    actual_price    = models.IntegerField()
    client_price    = models.IntegerField()


class Tour(models.Model):
    TOUR_TYPE = (
        ('1', 'Normal Tour'),
        ('2', 'Oficial Tour'),
        ('3', 'Honeymoon'),
    )
    title    = models.CharField(max_length=30)
    type     = models.CharField(max_length=1, choices=TOUR_TYPE, default=1)
    places   = models.CharField(max_length=200)
    duration_days   = models.CharField(max_length=3)
    duration_nights = models.CharField(max_length=3)
    members         = models.IntegerField()
    actual_price    = models.IntegerField()
    client_price    = models.IntegerField()


class Visa(models.Model):
    country_name    = models.CharField(max_length=30)
    processing_time = models.CharField(max_length=30)
    actual_price    = models.IntegerField()
    client_price    = models.IntegerField()


class PackageTour(models.Model):
    TOUR_TYPE = (
        ('1', 'Normal Tour'),
        ('2', 'Oficial Tour'),
        ('3', 'Honeymoon'),
    )
    client   = models.ForeignKey(Client, on_delete=models.CASCADE)
    title    = models.CharField(max_length=30)
    type     = models.CharField(max_length=1, choices=TOUR_TYPE, default=1)
    places   = models.CharField(max_length=200)
    duration_days   = models.CharField(max_length=3)
    duration_nights = models.CharField(max_length=3)
    members         = models.IntegerField()
    client_price    = models.IntegerField()
    paid_price      = models.IntegerField()
    due_price       = models.IntegerField()


class PackageIslamic(models.Model):
    TOUR_TYPE = (
        ('1', 'Hajj'),
        ('2', 'Umrah'),
    )
    client   = models.ForeignKey(Client, on_delete=models.CASCADE)
    title    = models.CharField(max_length=30)
    type     = models.CharField(max_length=1, choices=TOUR_TYPE, default=1)
    places   = models.CharField(max_length=200)
    duration_days   = models.CharField(max_length=3)
    duration_nights = models.CharField(max_length=3)
    members         = models.IntegerField()
    client_price    = models.IntegerField()
    paid_price      = models.IntegerField()
    due_price       = models.IntegerField()
    

class PackageAirTicket(models.Model):
    client         = models.ForeignKey(Client, on_delete=models.CASCADE)
    airline        = models.CharField(max_length=100)
    departure_from = models.CharField(max_length=100)
    departure_to   = models.CharField(max_length=100)
    client_price   = models.IntegerField()
    paid_price      = models.IntegerField()
    due_price       = models.IntegerField()
    

class PackageVisa(models.Model):
    client          = models.ForeignKey(Client, on_delete=models.CASCADE)
    country_name    = models.CharField(max_length=30)
    processing_time = models.CharField(max_length=30)
    client_price    = models.IntegerField()
    paid_price      = models.IntegerField()
    due_price       = models.IntegerField()
