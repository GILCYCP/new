from django.shortcuts import render
from facilities.models import Facilities
# Create your views here.
def facilities(request):
    if request.method=="POST":
        ob=Facilities()
        ob.equipments=request.POST.get('equipments')
        ob.special_features=request.POST.get('spl feautures')
        ob.save()
    return render(request,'facilities/register_facilities.html')




def viewfacilities(request):
    obj = Facilities.objects.all()
    context = {
        'f': obj
    }
    return render(request,'facilities/view_facilities.html',context)