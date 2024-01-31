from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
from django.shortcuts import render

from booking.models import Booking
from club.models import Club
from login.models import Login
# Create your views here.
def locate(request):
    obk=""
    if request.method=="POST":
        ob=Club()
        ob.club_name=request.POST.get('name')
        ob.address=request.POST.get('text')
        ob.email=request.POST.get('file')
        ob.phone=request.POST.get('number')
        ob.fees=request.POST.get('fees')
        ob.more_information=request.POST.get('more')
        ob.facilities=request.POST.get('fec')

        myfile = request.FILES['pic']
        fs = FileSystemStorage()
        file = fs.save(myfile.name, myfile)
        ob.img = myfile.name

        ob.password=request.POST.get('password')
        ob.status='pending'
        ob.save()

        ab=Login()
        ab.username = ob.club_name
        ab.password = ob.password
        ab.type = "club"
        ab.user_id = ob.club_id
        ab.save()
        obk="successfully registerd"
    context={
        'msg':obk
    }

    return render(request, 'club/club_registration.html',context)

def manage(request):
    obj = Club.objects.all()
    context = {
        'c': obj
    }
    return render(request,'club/Manage_club.html',context)

def apprv(request,idd):
    obj=Club.objects.get(club_id=idd)
    obj.status="approved"
    obj.save()
    return manage(request)


def reject(request,idd):
    obj=Club.objects.get(club_id=idd)
    obj.status="rejected"
    obj.save()
    return manage(request)



def userview(request):
    obj = Club.objects.filter(status="approved")
    context = {
        'c': obj
    }
    return render(request,'club/book.html',context)



def book(request,idd):
    # ob=Club.objects.get(club_id=idd)
    # context={
    #     'ok':ob
    # }
    ss=request.session["uid"]
    if request.method=="POST":
        obj=Booking()
        obj.to_time=request.POST.get('s')
        obj.from_time=request.POST.get('f')
        obj.date=request.POST.get('d')
        obj.user_id=ss
        # obj.club_id=idd
        obj.type='club'
        obj.save()

        # return
        return HttpResponseRedirect('/payment/payment/'+idd)
    return render(request,'booking/sheduledateandtime.html')



