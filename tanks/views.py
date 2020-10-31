from django.shortcuts import render, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy

from django.contrib.auth.models import User
from .forms import TankForm, FertilizerForm, UserCreateForm
from .models import Tank, Fertilizer
# Create your views here.


def index(request):
    return HttpResponse('This is the index')


class SignUpView(CreateView):
    form_class = UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


@login_required()
def tankcreation(request, form):
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
                return HttpResponseRedirect(reverse('tank-list'))
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
                return HttpResponseRedirect(reverse('tank-list'))

    else:
        return HttpResponse(404)


@login_required()
def tanklist(request):
    if request.user.is_authenticated:
        tanklist = Tank.objects.all().filter(owner_id=request.user.id)
        if request.method == 'GET':
            form = TankForm
            tlist = {'tanks': tanklist, 'form': form}
            return render(request, 'tanks/tank-list.html', context=tlist)
        elif request.method == 'POST':
            form = TankForm(request.POST)
            if form.is_valid():
                alias = request.POST['alias']
                gallons = request.POST['gallons']
                user_id = User.objects.get(pk=request.user.id)
                newTank = Tank(owner_id=user_id, alias=alias, gallons=gallons)
                newTank.save()
                return HttpResponseRedirect(reverse('tank-list'))
    else:
        return render(request, 'tanks/index.html')


@login_required()
def updatetank(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            tank = Tank.objects.get(pk=id)
            form = TankForm()
            form = TankForm(initial={'alias': tank.alias,
                                     'gallons': tank.gallons,
                                     })
            return render(request, 'tanks/tank-update.html', {'form': form})
        elif request.method == 'POST':
            form = TankForm(request.POST)
            if form.is_valid():
                tank = Tank.objects.get(pk=id)
                tank.alias = form.cleaned_data['alias']
                tank.gallons = form.cleaned_data['gallons']
                tank.save()
                return HttpResponseRedirect(reverse('tank-list'))

    else:
        return render(request, 'tanks/index.html')


@login_required()
def deletetank(request, id):
    if request.user.is_authenticated:
        if request.method == 'GET':
            tank = Tank.objects.get(pk=id)
            return render(request, 'tanks/tank-delete.html', {'tank': tank})
        elif request.method == 'POST':
            Tank.objects.filter(pk=id).delete()
            return HttpResponseRedirect(reverse('tank-list'))
    else:
        return render(request, 'tanks/index.html')