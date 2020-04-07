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
    contact = Txttobool(request.POST.get('contact_infected',''))
    loc_ini_stop = Segment.objects.get(
        id_route=request.POST.get('route',''),
        initial_stop=request.POST.get('initial_stop',''),
        direction=request.POST.get('direction',''),
        ).loc
    loc_end_stop = Segment.objects.get(
        id_route=request.POST.get('route',''),
        end_stop=request.POST.get('end_stop',''),
        direction=request.POST.get('direction',''),
        ).loc

    route = Route.objects.get(id=request.POST.get('route',''))
    direction = Direction.objects.get(id=request.POST.get('direction',''))
    initial_stop = Stop.objects.get(id=request.POST.get('initial_stop',''))
    end_stop = Stop.objects.get(id=request.POST.get('end_stop',''))
    bus_service = Bus_Segment.objects.get(id=request.POST.get('service',''))
    first_segment = Segment.objects.get(initial_stop_id=initial_stop, id_route=route, direction=direction)
    last_segment = Segment.objects.get(end_stop_id=end_stop, id_route=route, direction=direction)
    segments = Bus_Segment.objects.filter(service = bus_service.service,id_segment__gte = first_segment,id_segment__lte = last_segment)
    max_ocupation = Bus.objects.get(id=bus_service.id_bus.id)

    print(bus_service.id_bus, bus_service)

    actual_ocup = 0
    for seg in segments:
        if actual_ocup <= seg.passengers:
            actual_ocup = seg.passengers

    print (max_ocupation.safe_capacity, actual_ocup)

    if actual_ocup < int(max_ocupation.safe_capacity):
        Person_object = Person(
            gender = request.POST.get('gender',''),
            age = request.POST.get('age',''),
            email = request.POST.get('email',''), 
            preconditions = condition,
            contact_infected = contact,
            ocupation = request.POST.get('ocupation',''),
            destination_activities = request.POST.get('destination_activities', ''),
            home_address = request.POST.get('home_address', ''),
            destination_address = request.POST.get('destination_address',''),
            route = route,
            direction = direction,
            initial_stop = initial_stop,
            end_stop = end_stop,
            service = bus_service,
        )

        Person_object.save()
        
        last_person = Person.objects.latest('id').id

        for seg in segments:
            bus_service = Bus_Segment.objects.get(id=seg.id)
            bus_service.passengers += 1
            bus_service.save()
        
        return JsonResponse({})
    else:
        return JsonResponse({'error', 'error'})

def Save_person_no_route(request):
    condition = Txttobool(request.POST.get('preconditions',''))
    contact = Txttobool(request.POST.get('contact_infected',''))
    route = Route.objects.get(id=2)
    direction = Direction.objects.get(id=3)
    initial_stop = Stop.objects.get(id=6)
    end_stop = Stop.objects.get(id=6)
    bus_service = Bus_Segment.objects.get(id=21)

    try:
        Person_object = Person(
            gender = request.POST.get('gender',''),
            age = request.POST.get('age',''),
            email = request.POST.get('email',''), 
            preconditions = condition,
            contact_infected = contact,
            ocupation = request.POST.get('ocupation',''),
            destination_activities = request.POST.get('destination_activities', ''),
            home_address = request.POST.get('home_address', ''),
            destination_address = request.POST.get('destination_address',''),
            route = route,
            direction = direction,
            initial_stop = initial_stop,
            end_stop = end_stop,
            service = bus_service,
        )

        Person_object.save()

        return JsonResponse({})
    except:
        return JsonResponse({'error', 'error'})