from django.shortcuts import render
from login.models import Login
from django.http import HttpResponseRedirect

# Create your views here.

def login(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        password = request.POST.get('ps')
        obj =Login.objects.filter(username=name,password=password)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.user_id
            if tp == "admin":
                request.session["uid"]=uid
                return HttpResponseRedirect('/temp/admn/')
            elif tp == "user":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/user/')
            elif tp == "club":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/club/')
            elif tp == "shop":
                request.session["uid"] = uid
                return HttpResponseRedirect('/temp/shop/')
            else:
                objilist = "incorrect username or password....please try again..!"
                context = {
                    'mag' : objilist,
                }
                return render(request, 'login/login.html',context)

    return render(request,'login/login.html')


from rest_framework.views import APIView,Response
from login.serializers import android_serializers

class loginview(APIView):
    def get(self,request):
        ob=Login.objects.all()
        ser=android_serializers(ob,many=True)
        return Response(ser.data)

    def post(self,request):
        username=request.data['username']
        password=request.data['password']
        ob=Login.objects.filter(username=username,password=password)
        ser=android_serializers(ob,many=True)
        return Response(ser.data)