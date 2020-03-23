from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from covit.models import *
import traceback

# Utils

def Remove_duplicate(duplicate): 
    final_list = [] 
    for num in duplicate: 
        if num not in final_list: 
            final_list.append(num) 
    return final_list

def Txttobool(texto):
    if texto == 'true':
        return True
    else:
        return False

# Create your views here.

def Home(request):
    return render(request, 'home.html')

def Directions(request, route):
    directions = Direction.objects.filter(id_route=route)

    direc=[]

    for dire in directions:
        direc.append((str(dire), dire.id))
        direc.append((str(dire), dire.id))

    direc = Remove_duplicate(direc)
    
    return JsonResponse(direc, safe=False)

def Stops_direction(request, route, direction):
    segments = Segment.objects.filter(id_route=route, direction=direction)

    stops=[]

    for seg in segments:
        stops.append((str(seg.initial_stop), seg.initial_stop.id))
        stops.append((str(seg.end_stop), seg.end_stop.id))

    stops = Remove_duplicate(stops)
    
    return JsonResponse(stops, safe=False)

    

def Stops_ahead(request, route, initial_stop, direction):
    segment_ini = Segment.objects.get(id_route=route, initial_stop=initial_stop, direction=direction)
    loc_ini_stop = segment_ini.loc
    segments = Segment.objects.filter(id_route=route, direction=direction, loc__gt=loc_ini_stop)

    stops=[]

    for seg in segments:
        stops.append((str(seg.initial_stop), seg.initial_stop.id))
        stops.append((str(seg.end_stop), seg.end_stop.id))

    stops = Remove_duplicate(stops)
    
    return JsonResponse(stops, safe=False)

def Services(request, route, initial_stop, direction):
    segment_ini = Segment.objects.get(id_route=route, initial_stop=initial_stop, direction=direction)
    Bus_services = Bus_Segment.objects.filter(id_segment=segment_ini.id)
    
    services = []

    for service in Bus_services:
        services.append((service.start_hour, service.id))

    return JsonResponse(services, safe=False)

def Save_person_route(request):
    condition = Txttobool(request.POST.get('preconditions',''))
    contact = Txttobool(request.POST.get('contact',''))
    
    # try:
    Person_object = Person(
        gender=request.POST.get('gender',''),
        age=request.POST.get('age',''),
        preconditions=condition,
        contact_infected=contact,
        ocupation=request.POST.get('ocupation',''),
        destination_activities=request.POST.get('destination_activities', ''),
        home_address=request.POST.get('home_address', ''),
        destination_address=request.POST.get('destination_address',''),
    )
    Person = Person_object.save()

    print (Person.id)

    # except Exception as e:
    #     print (e)

    return render(request, 'home.html')
