from django.shortcuts import render,redirect
from . models import *
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def index(request):
    return render(request,'index.html')

# def contact(request):
#     return render(request,'contact.html')

def contact(request):
    if request.method=="POST":
            name=request.POST['name']
            email=request.POST['email']
            sub=request.POST['subject']
            phone=request.POST['phone']
            msg=request.POST['msg']

            add=contact(name=name,email=email,subject=sub,phone=phone,msg=msg)
            add.save()

            # email function

            subject = 'Contact Form'
            message = f'There is message from {name} email {email}. The message is {msg}. Thankyou.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [settings.EMAIL_HOST_USER, ] 
            send_mail( subject, message, email_from, recipient_list ) 
            # x = ''.join(random.choices(name + string.digits, k=8))
            # y = ''.join(random.choices(string.ascii_letters + string.digits, k=7))
            subject = ' thank for submitting Contact Form'
            message = f'Hi {name}, Thankyou for submitting form.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email, ] 
            send_mail( subject, message, email_from, recipient_list )

            return render(request,'contact.html',{"success":"Successfully submitted the information..."})
    else:
            return render(request,'contact.html')

def login(request):
    if request.method=="POST":        
        login_em=request.POST['Email']
        login_pswd=request.POST['Password']        
        check=register_tb.objects.filter(email=login_em,password=login_pswd)
        if check:
            for x in check:
                request.session["uid"]=x.id
                request.session["uname"]=x.name
            return render(request,"index.html")
        else:
            
            return render(request,"login.html",{"error":"not a registerd user"})
    else:
        return render(request,'login.html')

def about(request):
    if request.session.has_key('uid'):
        return render(request,'about.html')
    else:
        return redirect('/login/')

def payment(request):
    return render(request,'payment.html')

def register(request):
    if request.method=="POST":
            username=request.POST['uname']
            email=request.POST['Email']
            password=request.POST['Password']
            cpassword=request.POST['ConfirmPassword']

            print(username,email,password,cpassword)
            check=register_tb.objects.filter(email=email)

            if password==cpassword:
                if check:
                    return render(request,"register.html",{"error":"email already registered"})
                else:
                    add=register_tb(name=username,email=email,password=password)
                    add.save()
                    return render(request,'login.html',{"success":"Successfully submitted the information..."})
            else:
                return render(request,'register.html',{"error":"Password and Confirm password mismatch..."})
    else:
        return render(request,"register.html")
def typography(request):
    return render(request,'typography.html')

def logout(request):
    if request.session.has_key('uid'):
        del request.session["uid"]
        del request.session["uname"]
        return redirect('/login/')
    else:
        return redirect('/login/')