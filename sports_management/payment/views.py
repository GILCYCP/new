from django.shortcuts import render
from payment.models import Payment
# Create your views here.
def payment(request,idd):
    ss=request.session["uid"]
    context={
        'k':idd
    }
    if request.method == "POST":
        ob = Payment()
        ob.user_id=ss
        ob.account_number = request.POST.get('number')
        ob.contact_number = request.POST.get('co')
        ob.amount = request.POST.get('pp')
        ob.ifsc_code=request.POST.get('text')
        ob.type='club'
        ob.save()
    return render(request,'payment/payment.html',context)





def item(request,idd):
    ss=request.session["uid"]
    context={
        'u':idd
    }
    if request.method == "POST":
        ob = Payment()
        ob.user_id=ss
        ob.account_number = request.POST.get('acc')
        ob.contact_number = request.POST.get('number')
        ob.amount = request.POST.get('aaa')
        ob.type='shop'
        ob.ifsc_code=request.POST.get('if')
        ob.save()
    return render(request,'payment/itempay.html',context)






def viewpayment(request):
    obj = Payment.objects.filter(type='club')
    context = {
        'p': obj
    }
    return render(request,'payment/clubview_payment.html', context)


def paprl(request,idd):
    obj =Payment.objects.get(payment_id=idd)
    obj.status = "paid"
    obj.save()
    return viewpayment(request)

def prejt(request,idd):
    obj =Payment.objects.get(payment_id=idd)
    obj.status = "not paid"
    obj.delete()
    return viewpayment(request)

def shopviewpayment(request):
    obj = Payment.objects.filter(type='shop')
    context = {
        'sp': obj
    }
    return render(request, 'payment/shopviewpayment.html', context)

def s1(request,idd):
    obj =Payment.objects.get(payment_id=idd)
    obj.status = "paid"
    obj.save()
    return shopviewpayment(request)

def s2(request,idd):
    obj =Payment.objects.get(payment_id=idd)
    obj.status = "not paid"
    obj.delete()
    return shopviewpayment(request)
