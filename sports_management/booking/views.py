from django.shortcuts import render
from booking.models import Booking
from django.http import HttpResponseRedirect
from payment.models import Payment
from django.core.files.storage import FileSystemStorage
from club.models import Club
# Create your views here.
def online(request):
    if request.method=="POST":
        obj=Booking()
        obj.address=request.POST.get('text')

        mfile = request.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(mfile.name,mfile)
        obj.image=mfile.name
        obj.club_name=request.POST.get('name')
        obj.more_information=request.POST.get('info')
        obj.facilities=request.POST.get('facility')
        obj.working_time=request.POST.get('time')
        obj.amount=request.POST.get('rupees')
        # obj.user_id='1'
        obj.save()
    return render(request,'booking/club_registering.html')

def viewbooking(request):
    # ss = request.session["uid"]
    obj = Booking.objects.all()
    context = {
        'b': obj
    }
    return render(request, 'booking/booking_satus.html', context)

def mngbooking(request):
    ob = Payment.objects.all()
    obj =Booking.objects.all()
    context = {
        'b': obj,
        'p':ob
    }
    return render(request,'booking/manage_booking.html',context)

def aprl(request,idd):
    obj =Booking.objects.get(booking_id=idd)
    obj.status = "approved"
    obj.save()
    return mngbooking(request)

def rejt(request,idd):
    obj =Booking.objects.get(booking_id=idd)
    obj.status = "reject"
    obj.save()
    return mngbooking(request)

# def clubbkg(request):
#     obj = Booking.objects.all()
#     context = {
#         'o': obj
#     }
#     return render(request,'booking/clubbooking.html',context)

# def book(request,idd):
#     ss=request.session["uid"]
#     if request.method=="POST":
#         obj=Booking()
#         obj.to_time=request.POST.get('t')
#         obj.from_time=request.POST.get('f')
#         obj.date=request.POST.get('d')
#         obj.user_id=ss
#         obj.type='club'
#         obj.save()
#
#         # return
#         return HttpResponseRedirect('/payment/payment/'+str(obj.amount))
#     return render(request,'booking/sheduledateandtime.html')


# def clubregi(request,idd):
#     obj = Booking.objects.get(booking_id=idd)
#     context = {
#         'o': obj,
#     }
#     if request.method=="POST":
#         obj=Booking.objects.get(booking_id=idd)
#         obj.to_time=request.POST.get('t')
#         obj.from_time=request.POST.get('f')
#         obj.date=request.POST.get('d')
#         obj.save()
#         return HttpResponseRedirect('/bookin/clubbkng/')
#     return render(request,'booking/club_registering.html',context)