from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from .forms import TankForm, FertilizerForm
from .models import Tank, Fertilizer
# Create your views here.


def index(request):
    return HttpResponse('This is the index')


@login_required()
def tankcreation(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = TankForm()
            return render(request, 'tanks/tank-create.html', {'form': form})
        elif request.method == 'POST':
            form = TankForm(request.POST)
            if form.is_valid():
                gallons = request.POST['gallons']
                alias = request.POST['alias']
                user_id = User.objects.get(pk=request.user.id)
                tank = Tank(owner_id=user_id, alias=alias, gallons=gallons)
                tank.save()
                return HttpResponse('EUREKA')
    else:
        return HttpResponse('Not logged in')

@login_required()
def fertilizercreation(request):
    if request.user.is_authenticated:
        if request.method == 'GET':
            form = FertilizerForm()
            return render(request, 'tanks/fertilizer-create.html', {'form': form})
        elif request.method == 'POST':
            form = FertilizerForm(request.POST)
            if form.is_valid():
                brand = request.POST['brand']
                typeFertilizer = request.POST['type']
                tank_id = Tank.objects.get(pk=1, owner_id=request.user.id)
                fertilizer = Fertilizer(brand=brand, type=typeFertilizer, tank_id=tank_id)
                fertilizer.save()
                return HttpResponse('EUREKA')
    else:
        return HttpResponse(404)