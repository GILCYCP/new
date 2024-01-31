from django.shortcuts import render

# Create your views here.
def admin(request):
    return render(request,'temp/admin.html')

def club_manage(request):
    return render(request,'temp/club manage.html')

def home(request):
    return render(request,'temp/home.html')

def shop(request):
    return render(request,'temp/shop.html')


def user(request):
    return render(request,'temp/user.html')



