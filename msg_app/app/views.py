from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from app.forms import ContactForm
from django.core.mail import send_mail, BadHeaderError
from django.contrib import messages
from .forms import NewUserForm
from django.contrib.auth import login


# Create your views here.
def homepage(request):
    return render(request, "home.html")

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccess ful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":form})

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body = {
                'first_name': form.cleaned_data['first_name'],
                'last_name': form.cleaned_data['last_name'],
                'email': form.cleaned_data['email_address'],
                'message': form.cleaned_data['message'],}
            message = "\n".join(body.values())
            # try:
                # send_mail(subject,message,'admin@example.com',['admin@example.com'])
            # except BadHeaderError:
                # return HttpResponse('Invalid header')
            # messages.success(request, "Message sent")
            # try: 
            print("Email sent..!", message)
            # except NameError:
            messages.success(request,"Message is sent succesfully")
            return redirect("contact")
    form = ContactForm()
    return render(request, "contact.html", {'form':form})
    # return render(request, "contact.html", {}) 
    
    
# ----------------------------------------***--------------
    
from django.http import HttpResponse

# Create your models here.
# -----------------------changes are made for understanding git functionality
from django.contrib.auth import login, logout,authenticate
def user_login(request):
    if request.method == 'POST':
        username= request.POST.get('username') 
        password= request.POST.get('password')
        print(username, password)
        user = authenticate(username, password)
        if user:
            login(request, user)
            return HttpResponse("successfully logged in")
            

        

# -------------------changes by saytm--------
def product_videos(request):
    print("in product videos")
    
    
# -----------------changes made by rashmi -----

def f1(x,y):
    return x+y


c = f1(3,4)
print(c)    
#------------------------------------------ 