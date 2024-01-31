from django.shortcuts import render
from delivery_status.models import DeliveryStatus
# Create your views here.
def delivery(request):
    if request.method=="POST":
        ob=DeliveryStatus()
        ob.product_name=request.POST.get('text')
        ob.delivery_date=request.POST.get('DATE')
        ob.time=request.POST.get('TIME')
        ob.status=request.POST.get('status')
        ob.save()
    return render(request,'delivery_status/delivery_status.html')




def viewdelivery(request):
    ss=request.session["uid"]
    obj = DeliveryStatus.objects.all()
    context = {
        'd': obj
    }
    return  render(request,'delivery_status/view _delivery_status.html',context)