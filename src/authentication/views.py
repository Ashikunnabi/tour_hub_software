# from bug_tracker import credentials
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect

from .decorators import has_access

        
def login_view(request):
    """     Login      """
    if request.method == "POST":                        # If method=POST then request is valid otherwise not
        employee_id = request.POST['employeeID']        # Collecting employee id
        password    = request.POST['password']          # Collecting password
        user = authenticate(username=employee_id, password=password) # If user is valid then authenticte otherwise not
        if user is not None:
            login(request, user)                        # If valid user then login
            return redirect('index')            
        else:                                           # If username / password is wrong
            context={"error": "Invalid Employee I / Password."}
            return render(request, 'authentication/login.html', context)
    else:
        if request.user.is_authenticated:
            return redirect('/')
        else:
            return render(request, 'authentication/login.html')
    
    
@login_required(login_url='login')   
@has_access(allowed_roles=['admin', 'employee'])
def logout_view(request):
    """ Logout for all users """
    logout(request)
    return redirect(login_view)    
    
    
   
@login_required(login_url='login')
@has_access(allowed_roles=['admin', 'employee'])
def index_view(request): 
    if request.user.groups.all()[0].name == ('admin'):
        return redirect('m_index')
    elif request.user.groups.all()[0].name == 'employee':
        return redirect('e_index')
    else:
        context={"error": "Invalid Employee ID / Password."}
        return render(request, 'authentication/login.html', context)


       