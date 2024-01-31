from django.http import HttpResponseRedirect
from django.shortcuts import render

from delivery_status.models import DeliveryStatus
from order.models import Order
# Create your views here.
# def placeorder(request):
#     if request.method == "POST":
#         ob =Order()
#         ob.user_id='1'
#         ob.sportsitem_name = request.POST.get('text')
#         ob.amount = request.POST.get('number')
#         ob.image = request.POST.get('file')
#         ob.account_number=request.POST.get('accno')
#         ob.save()
#
#     return render(request, 'order/add_sportsitems.html')




def vieworder(request):
    ss=request.session["uid"]
    obj = Order.objects.filter(user_id=ss)
    context = {
        'o': obj
    }
    return render(request,'order/view_order.html',context)

def mngorder(request):
    obj =Order.objects.all()
    context = {
        'o': obj
    }
    return render(request,'order/manage_order.html',context)

def aprl(request,idd):
    obj =Order.objects.get(order_id=idd)
    obj.status = "approved"
    obj.save()
    return HttpResponseRedirect('/delivery_status/delivery/')

def rejt(request,idd):
    obj =Order.objects.get(order_id=idd)
    obj.status = "reject"
    obj.delete()
    return mngorder(request)


def delivery(request,idd):
    obj=Order.objects.get(order_id=idd)
    context={
        'ok':obj
    }
    if request.method=="POST":
        ob=DeliveryStatus()
        # ob.product_name
        ob.delivery_date=request.POST.get('DATE')
        ob.order_id=idd
        ob.time=request.POST.get('TIME')
        ob.status=request.POST.get('status')
        ob.save()
    return render(request,'delivery_status/delivery_status.html',context)
