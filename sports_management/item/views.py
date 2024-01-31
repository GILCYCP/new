from django.shortcuts import render
from item.models import Item
from order.models import Order
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponseRedirect
# Create your views here.
def item(request):
    if request.method == "POST":
        mfile = request.FILES['itemimage']
        fs = FileSystemStorage()
        file = fs.save(mfile.name, mfile)
        ob =Item()
        ob.item_name = request.POST.get('text')
        ob.amount = request.POST.get('number')
        ob.image=mfile.name
        ob.save()
    return render(request,'item/add_item.html')

def viewitem(request):
    obj = Item.objects.all()
    context = {
        'pp': obj
    }
    return render(request,'item/view_sportsitem.html',context)










def order(request,idd):
    ss=request.session["uid"]
    ob = Item.objects.get(item_id=idd)
    context = {
        'pp': ob
    }
    if request.method=="POST":
        a=ob.item_name
        b=ob.amount
        c=ob.image
        obj=Order()
        obj.amount=b
        obj.sportsitem_name=a
        obj.image=c
        obj.user_id=ss
        obj.save()
        return HttpResponseRedirect('/payment/itempay/'+str(obj.amount))
    return render(request,'order/order.html',context)