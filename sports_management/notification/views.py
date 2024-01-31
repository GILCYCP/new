from django.shortcuts import render
from notification.models import Notification
# Create your views here.
def postnotification(request):
    if request.method == "POST":
        ob = Notification()
        ob.notification= request.POST.get('text')
        ob.save()
    return render(request,'notification/post_notification.html')

def postnotification_shop(request):
    if request.method == "POST":
        ob = Notification()
        ob.notification= request.POST.get('text')
        ob.save()
    return render(request,'notification/shop_notification.html')




def viewnotificatin(request):
    obj = Notification.objects.all()
    context = {
        'n': obj
    }
    return render(request,'notification/view_notification.html',context)