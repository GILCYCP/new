from django.shortcuts import render
from shop.models import Shop
from login.models import Login
# Create your views here.
def shop(request):
    obk=""
    if request.method == "POST":
        ob =Shop()
        ob.shop_name = request.POST.get('name')
        ob.address= request.POST.get('address')
        ob.mob_no=request.POST.get('num')
        ob.password = request.POST.get('password')
        ob.save()

        ab =Login()
        ab.username = ob.shop_name
        ab.password = ob.password
        ab.type = "shop"
        ab.user_id = ob.shop_id
        ab.save()
        obk="successfully registerd"
    context={
        'msg':obk
    }
    return render(request,'shop/shop_registration.html',context)


def shop_view(request):
    obj = Shop.objects.filter(status="approved")
    context = {
        's': obj
    }
    return render(request,'shop/shop.html',context)

def mngshop(request):
    obj = Shop.objects.all()
    context = {
        'k': obj
    }
    return render(request,'shop/manageshop.html',context)

def apprv(request,idd):
    obj =Shop.objects.get(shop_id=idd)
    obj.status = "approved"
    obj.save()
    return mngshop(request)

def rejt(request,idd):
    obj =Shop.objects.get(shop_id=idd)
    obj.status = "reject"
    obj.delete()
    return mngshop(request)
