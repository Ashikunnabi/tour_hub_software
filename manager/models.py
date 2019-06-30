from django.db import models


class Employee(models.Model):
    TYPE = (
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    )
    STATUS = (
        ('1', 'Married'),
        ('2', 'Unmarried'),
    )
    type                 = models.CharField(max_length=10, choices=TYPE, default='employee') 
    employee_id          = models.CharField(max_length=50)
    password             = models.CharField(max_length=100)
    name                 = models.CharField(max_length=50)
    phone_number         = models.CharField(max_length=15)
    email                = models.EmailField()
    present_address      = models.CharField(max_length=200)
    permanent_address    = models.CharField(max_length=200)
    nid                  = models.IntegerField()
    dob                  = models.DateField(auto_now=False, auto_now_add=False)
    designation          = models.CharField(max_length=50)
    photo                = models.FileField(blank=True, null=True)
    marital_status       = models.CharField(max_length=1, choices=STATUS, default='2')    
    
    def __str__(self):
        return self.employee_id
        

class Client(models.Model):
    created_by           = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at           = models.DateField(auto_now_add=True)
    name                 = models.CharField(max_length=50)
    phone                = models.IntegerField()
    email                = models.EmailField(blank=True, null=True)
    profession           = models.CharField(max_length=50,blank=True, null=True)
    address              = models.CharField(max_length=200, blank=True, null=True)
    photo                = models.FileField(blank=True, null=True)
    
    def __str__(self):
        return ("{} - 0{}").format(self.name,self.phone)


class EnquiryClient(models.Model):
    TOUR_TYPE = (
        ('1', 'Normal Tour'),
        ('2', 'Oficial Tour'),
        ('3', 'Honeymoon'),
        ('4', 'Hajj'),
        ('5', 'Umrah'),
        ('6', 'Air Ticket'),
        ('7', 'Visa Processing'),
    )
    HOTEL_QUALITY = (
        ('1', '5*'),
        ('2', '3*'),
        ('3', '2*'),
    )
    HAS_VISA = (
        ('1', 'Yes'),
        ('2', 'No'),
    )
    STATUS = (
        ('1', 'Confirm'),
        ('2', 'Cancel'),
    )
    created_by        = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at        = models.DateField(auto_now_add=True)
    name              = models.CharField(max_length=50)
    phone             = models.IntegerField()
    email             = models.EmailField(blank=True, null=True)
    profession        = models.CharField(max_length=50, blank=True, null=True)
    address           = models.CharField(max_length=200, blank=True, null=True)
    type              = models.CharField(max_length=1, choices=TOUR_TYPE, blank=True, null=True)
    country_name      = models.CharField(max_length=30, blank=True, null=True)
    places            = models.CharField(max_length=200, blank=True, null=True)
    members           = models.IntegerField(blank=True, null=True)
    child             = models.IntegerField(blank=True, null=True)
    infant            = models.IntegerField(blank=True, null=True)
    hotel_quality     = models.CharField(max_length=1, choices=HOTEL_QUALITY, blank=True, null=True)
    number_of_rooms   = models.IntegerField(blank=True, null=True)
    duration          = models.CharField(max_length=30, blank=True, null=True)
    by_air_route      = models.CharField(max_length=100, blank=True, null=True)
    visa_detail       = models.CharField(max_length=1, choices=HAS_VISA, default='2')
    previous_tour     = models.CharField(max_length=300, blank=True, null=True)
    special_requirment= models.CharField(max_length=1000, blank=True, null=True)
    client_price      = models.IntegerField(blank=True, null=True)  
    follow_up_date_01 = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    update_01         = models.CharField(max_length=300, blank=True, null=True)
    follow_up_date_02 = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    update_02         = models.CharField(max_length=300, blank=True, null=True)
    follow_up_date_03 = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    update_03         = models.CharField(max_length=300, blank=True, null=True)
    follow_up_date_04 = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    update_04         = models.CharField(max_length=300, blank=True, null=True)
    follow_up_date_05 = models.DateField(auto_now_add=False, auto_now=False, blank=True, null=True)
    update_05         = models.CharField(max_length=300, blank=True, null=True)
    status            = models.CharField(max_length=1, choices=STATUS, blank=True, null=True)
    reason_of_cancel  = models.CharField(max_length=500, blank=True, null=True)
    do_register       = models.BooleanField(default=False)
    
    def __str__(self):
        return self.name


class AirPort(models.Model):
    created_by     = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at     = models.DateField(auto_now_add=True)
    name           = models.CharField(max_length=200)
    country        = models.CharField(max_length=100) 
    
    
    def __str__(self):
        return self.name


class AirTicket(models.Model):
    created_by     = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at     = models.DateField(auto_now_add=True)
    airline        = models.CharField(max_length=100)
    departure      = models.CharField(max_length=100)
    arrival        = models.CharField(max_length=100)
    quantity       = models.IntegerField(default=1)
    actual_price   = models.IntegerField(default=0, blank=True)
    client_price   = models.IntegerField()


class Islamic(models.Model):
    TOUR_TYPE = (
        ('1', 'Hazz'),
        ('2', 'Umrah'),
    )
    created_by      = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at      = models.DateField(auto_now_add=True)
    title           = models.CharField(max_length=30)
    type            = models.CharField(max_length=1, choices=TOUR_TYPE, default=1)
    places          = models.CharField(max_length=200)
    duration_days   = models.CharField(max_length=3)
    duration_nights = models.CharField(max_length=3)
    members         = models.IntegerField()
    actual_price    = models.IntegerField(default=0, blank=True)
    client_price    = models.IntegerField()


class Tour(models.Model):
    TOUR_TYPE = (
        ('1', 'Normal Tour'),
        ('2', 'Oficial Tour'),
        ('3', 'Honeymoon'),
    )
    created_by      = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at      = models.DateField(auto_now_add=True)
    title           = models.CharField(max_length=30)
    type            = models.CharField(max_length=1, choices=TOUR_TYPE, default=1)
    places          = models.CharField(max_length=200)
    duration_days   = models.CharField(max_length=3)
    duration_nights = models.CharField(max_length=3)
    members         = models.IntegerField()
    actual_price    = models.IntegerField(default=0, blank=True)
    client_price    = models.IntegerField()


class Visa(models.Model):
    created_by      = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at      = models.DateField(auto_now_add=True)
    country_name    = models.CharField(max_length=30)
    processing_time = models.CharField(max_length=30)
    actual_price    = models.IntegerField(default=0, blank=True)
    client_price    = models.IntegerField()


class PackageTour(models.Model):
    TOUR_TYPE = (
        ('1', 'Normal Tour'),
        ('2', 'Oficial Tour'),
        ('3', 'Honeymoon'),
    )
    HOTEL_QUALITY = (
        ('1', '5*'),
        ('2', '3*'),
        ('3', '2*'),
    )
    created_by      = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at      = models.DateField(auto_now_add=True)
    client          = models.ForeignKey(Client, on_delete=models.CASCADE)
    title           = models.CharField(max_length=30)
    type            = models.CharField(max_length=1, choices=TOUR_TYPE, default=1)
    places          = models.CharField(max_length=200)
    duration_days   = models.CharField(max_length=3)
    duration_nights = models.CharField(max_length=3)
    members         = models.IntegerField()
    child             = models.IntegerField(blank=True, null=True)
    infant            = models.IntegerField(blank=True, null=True)
    hotel_quality     = models.CharField(max_length=1, choices=HOTEL_QUALITY, blank=True, null=True)
    number_of_rooms   = models.IntegerField(blank=True, null=True)
    airline           = models.CharField(max_length=100, blank=True, null=True)
    special_requirment= models.CharField(max_length=200, blank=True, null=True)
    actual_price    = models.IntegerField(default=0, blank=True)
    client_price    = models.IntegerField()
    in_cart         = models.BooleanField(default=False)


class PackageIslamic(models.Model):
    TOUR_TYPE = (
        ('1', 'Hajj'),
        ('2', 'Umrah'),
    )
    HOTEL_QUALITY = (
        ('1', '5*'),
        ('2', '3*'),
        ('3', '2*'),
    )
    created_by      = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at      = models.DateField(auto_now_add=True)
    client          = models.ForeignKey(Client, on_delete=models.CASCADE)
    title           = models.CharField(max_length=30)
    type            = models.CharField(max_length=1, choices=TOUR_TYPE, default=1)
    places          = models.CharField(max_length=200)
    duration_days   = models.CharField(max_length=3)
    duration_nights = models.CharField(max_length=3)
    members         = models.IntegerField()
    child             = models.IntegerField(blank=True, null=True)
    infant            = models.IntegerField(blank=True, null=True)
    hotel_quality     = models.CharField(max_length=1, choices=HOTEL_QUALITY, blank=True, null=True)
    number_of_rooms   = models.IntegerField(blank=True, null=True)
    airline           = models.CharField(max_length=100, blank=True, null=True)
    special_requirment= models.CharField(max_length=200, blank=True, null=True)
    actual_price    = models.IntegerField(default=0, blank=True)
    client_price    = models.IntegerField()
    in_cart         = models.BooleanField(default=False)
    

class PackageAirTicket(models.Model):
    created_by     = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at     = models.DateField(auto_now_add=True)
    client         = models.ForeignKey(Client, on_delete=models.CASCADE)
    airline        = models.CharField(max_length=100)
    departure      = models.CharField(max_length=100)
    arrival        = models.CharField(max_length=100)
    quantity       = models.IntegerField(default=1)
    actual_price   = models.IntegerField(default=0, blank=True)
    client_price   = models.IntegerField()
    in_cart        = models.BooleanField(default=False)
    

class PackageVisa(models.Model):
    created_by      = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at      = models.DateField(auto_now_add=True)
    client          = models.ForeignKey(Client, on_delete=models.CASCADE)
    country_name    = models.CharField(max_length=30)
    processing_time = models.CharField(max_length=30)
    actual_price    = models.IntegerField(default=0, blank=True)
    client_price    = models.IntegerField()
    in_cart         = models.BooleanField(default=False)
    

class Cart(models.Model):
    created_by      = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at      = models.DateField(auto_now_add=True)
    package_tour    = models.ForeignKey(PackageTour, on_delete=models.CASCADE, blank=True, null=True)
    package_islamic = models.ForeignKey(PackageIslamic, on_delete=models.CASCADE, blank=True, null=True)
    package_air_ticket = models.ForeignKey(PackageAirTicket, on_delete=models.CASCADE, blank=True, null=True)
    package_visa    = models.ForeignKey(PackageVisa, on_delete=models.CASCADE, blank=True, null=True)
    

class Order(models.Model):
    PAYMENT_METHOD = (
        ('1', 'Cash'),
        ('2', 'Cheque'),
        ('3', 'DD'),
        ('4', 'TT'),
    )
    created_by         = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at         = models.DateField(auto_now_add=True)
    client             = models.ForeignKey(Client, on_delete=models.CASCADE)
    package_tour       = models.ForeignKey(PackageTour, on_delete=models.CASCADE, blank=True, null=True)
    package_islamic    = models.ForeignKey(PackageIslamic, on_delete=models.CASCADE, blank=True, null=True)
    package_air_ticket = models.ForeignKey(PackageAirTicket, on_delete=models.CASCADE, blank=True, null=True)
    package_visa       = models.ForeignKey(PackageVisa, on_delete=models.CASCADE, blank=True, null=True)
    payment_method     = models.CharField(max_length=1, choices=PAYMENT_METHOD, default='1')
    cheque_number      = models.CharField(max_length=30, blank=True)
    bank               = models.CharField(max_length=50, blank=True)
    branch             = models.CharField(max_length=50, blank=True)
    cheque_date        = models.CharField(max_length=30, blank=True)
    booking_id         = models.CharField(max_length=30, blank=True)
    actual_price       = models.IntegerField()
    total_ammount      = models.IntegerField()
    discount           = models.IntegerField(default=0)
    tax_rate           = models.CharField(max_length=4, default=0)
    total_tax          = models.IntegerField(default=0)
    shipping_handling  = models.IntegerField(default=0)
    payable_ammount    = models.IntegerField()
    received_ammount   = models.IntegerField()
    due_ammount        = models.IntegerField()    
    advertisement        = models.FileField(blank=True, null=True)

    
class Expenditure(models.Model):
    PAYMENT_METHOD = (
        ('1', 'Cash'),
        ('2', 'Cheque'),
    )
    created_at      = models.DateField(auto_now_add=True)
    made_by         = models.CharField(max_length=100)
    date            = models.CharField(max_length=20)
    by              = models.CharField(max_length=1, choices=PAYMENT_METHOD, default='1')
    being_the       = models.CharField(max_length=200, blank=True)
    description_01  = models.CharField(max_length=100, blank=True)
    cost_01         = models.IntegerField(default=0)
    description_02  = models.CharField(max_length=100, blank=True)
    cost_02         = models.IntegerField(default=0)
    description_03  = models.CharField(max_length=100, blank=True)
    cost_03         = models.IntegerField(default=0)
    description_04  = models.CharField(max_length=100, blank=True)
    cost_04         = models.IntegerField(default=0)
    description_05  = models.CharField(max_length=100, blank=True)
    cost_05         = models.IntegerField(default=0)
    total           = models.IntegerField()
    

class Marketing(models.Model):
    created_by      = models.ForeignKey(Employee, on_delete=models.CASCADE)
    created_at      = models.DateField(auto_now_add=True)
    category_name   = models.CharField(max_length=30)
    border_color    = models.CharField(max_length=30)
    file            = models.FileField()
    
    
    
    
    