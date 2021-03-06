
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView
from django.db.models import Max, Min, Count


from .models import SquirrelSighting
from .forms import SightingForm

def index(request):
    return HttpResponse("Index Page")

def map(request):
    sightings = SquirrelSighting.objects.all()[:100]
    context = {'sightings': sightings}
    return render(request, 'squirrel/map.html', context)

def sightings(request):
    squirrel = SquirrelSighting.objects.all()
    context = {'squirrel': squirrel}
    return render(request, 'squirrel/all.html', context)

def detail(request, unique_squirrel_id):
    squirrel = get_object_or_404(SquirrelSighting, unique_squirrel_id=unique_squirrel_id)
    form = SightingForm(request.POST or None, instance=squirrel)
    if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('squirrel:sightings'))
    return render(request, 'squirrel/detail.html', {'form': form})

def add(request):
    squirrel = SquirrelSighting()
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            squirrel = form.save()
            return HttpResponseRedirect(reverse('squirrel:sightings'))
    else:
        form = SightingForm()
    context = {'form': form, 'squirrel': squirrel}
    return render(request, 'squirrel/add.html', context)


def stats(request):
    squirrels = SquirrelSighting.objects.all()
    total_num = len(squirrels)
    latitude = squirrels.aggregate(minimum=Min('latitude'), maximum=Max('latitude'))
    longitude = squirrels.aggregate(minimum=Min('longitude'), maximum=Max('longitude'))
    shift = dict(squirrels.values_list('shift').annotate(Count('shift')))
    am = shift['AM']
    pm = shift['PM']
    age = len(squirrels.filter(age='Adult'))
    first = squirrels.aggregate(minimum=Min('date'))
    context = {'total': total_num,
               'latitude': latitude,
               'longitude': longitude,
               'am': am,
               'pm': pm,
               'age': age,
               'first': first,
    }
    return render(request, 'squirrel/stats.html', context)


