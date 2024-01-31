from django.shortcuts import render
from advertisement.models import Advertisement
from django.core.files.storage import FileSystemStorage
# Create your views here.
def post(request):
    if request.method=="POST":
        mfile = request.FILES['clubimage']
        fs = FileSystemStorage()
        file = fs.save(mfile.name, mfile)
        ob=Advertisement()
        ob.contact_number=request.POST.get('o')
        ob.product_image=request.POST.get('clubimage')
        ob.product_image = mfile.name
        ob.product_name=request.POST.get('name')
        ob.save()
    return render(request, 'advertisement/club_post_ads.html')


def post_shop(request):
    if request.method=="POST":
        mfile = request.FILES['shopimage']
        fs = FileSystemStorage()
        file = fs.save(mfile.name, mfile)
        ob = Advertisement()
        ob=Advertisement()
        ob.contact_number=request.POST.get('c')
        ob.product_image=request.POST.get('shopiimage')
        ob.product_image = mfile.name
        ob.product_name=request.POST.get('name')
        ob.save()
    return render(request, 'advertisement/shop_post_ads.html')


def post_shop_admin(request):
    if request.method=="POST":
        mfile = request.FILES['adminimage']
        fs = FileSystemStorage()
        file = fs.save(mfile.name, mfile)
        ob=Advertisement()
        ob.contact_number=request.POST.get('contact')
        ob.product_image=request.POST.get('adminimage')
        ob.product_image=mfile.name
        ob.product_name=request.POST.get('name')
        ob.save()
    return render(request, 'advertisement/admin_post_ads.html')






def viewads(request):
    obj=Advertisement.objects.all()
    context={
        'a':obj
    }
    return render(request, 'advertisement/view_advertisement.html', context)

def mngads(request):
    obj =Advertisement.objects.all()
    context = {
        'z': obj
    }
    return render(request, 'advertisement/admin_manage_ads.html', context)

def aprl(request,idd):
    obj =Advertisement.objects.get(ads_id=idd)
    obj.status = "approved"
    obj.save()
    return mngads(request)

def rejt(request,idd):
    obj =Advertisement.objects.get(ads_id=idd)
    obj.status = "reject"
    obj.delete()
    return mngads(request)