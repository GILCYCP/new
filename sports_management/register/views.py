from django.shortcuts import render
from register.models import Register
from login.models import Login
# Create your views here.
def register(request):
    obk=""
    if request.method=="POST":
        ob=Register()
        ob.user_name=request.POST.get('name')
        ob.email=request.POST.get('mail')
        ob.contact_number=request.POST.get('phone')
        ob.password=request.POST.get('password')
        ob.save()

        ab=Login()
        ab.username=ob.user_name
        ab.password=ob.password
        ab.type="user"
        ab.user_id=ob.user_id
        ab.save()
        obk="successfully registerd"
    context={
        'msg':obk
    }
    return render(request,'register/register.html',context)

def registerview(request):
    obj = Register.objects.all()
    context = {
        'r': obj
    }

    return render(request,'register/view register.html',context)
