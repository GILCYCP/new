from django.shortcuts import render
from games.models import Games
# Create your views here.
def addgame(request):
    if request.method == "POST":
        ob = Games()
        ob.game_name = request.POST.get('text')
        ob.game_points = request.POST.get('point')
        ob.save()
    return render(request,'games/add_game.html')



def viewgame(request):
    obj = Games.objects.all()
    context = {
        'g': obj
    }
    return render(request,'games/view_game.html',context)