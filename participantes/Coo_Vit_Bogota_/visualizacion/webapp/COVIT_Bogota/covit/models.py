from django.db import models

# Create your models here.
class Route(models.Model):
    name = models.TextField(max_length=50)
    headway = models.DecimalField(max_digits=4, decimal_places=1)
    date = models.DateField()
    start_hour = models.TimeField()
    end_hour = models.TimeField()

class Bus(models.Model):
    normal_capacity = models.IntegerField()
    safe_capacity = models.IntegerField()
    id_route = models.ForeignKey(Route, null=False, on_delete=models.CASCADE)
    service_datetime = models.TimeField(null=True, blank=True)

class Stop(models.Model):
    id_route = models.ForeignKey(Route, null=False, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    longitud = models.DecimalField(max_digits=20, decimal_places=10)
    latitude = models.DecimalField(max_digits=20, decimal_places=10)

    def __str__(self):
        return self.name

class Direction(models.Model):
    id_route = models.ForeignKey(Route, null=False, on_delete=models.CASCADE)
    direction = models.TextField(max_length=50)

    def __str__(self):
        return self.direction

    
class Segment(models.Model):
    id_route = models.ForeignKey(Route, null=False, on_delete=models.CASCADE)
    initial_stop = models.ForeignKey(Stop, null=False, related_name='stop_initial',on_delete=models.CASCADE)
    end_stop = models.ForeignKey(Stop, null=False, related_name='stop_end',on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    #direction = models.TextField(max_length=50)
    direction = models.ForeignKey(Direction, null=False, related_name='stop_end',on_delete=models.CASCADE)
    loc = models.IntegerField()

class Bus_Segment(models.Model):
    id_bus = models.ForeignKey(Bus, null=False, on_delete=models.CASCADE)
    id_segment = models.ForeignKey(Segment, null=False, on_delete=models.CASCADE)
    start_hour = models.TimeField()
    end_hour = models.TimeField()
    passengers = models.IntegerField()

class Person(models.Model):
    gender = models.TextField(max_length=5)
    age = models.IntegerField(null=True)
    preconditions = models.BooleanField()
    contact_infected = models.BooleanField()
    ocupation = models.TextField(max_length=50)
    destination_activities = models.TextField(max_length=50)
    home_address = models.TextField(max_length=50)
    destination_address = models.TextField(max_length=50)

class Trip(models.Model):
    id_person = models.ForeignKey(Person, null=False, on_delete=models.CASCADE)
    id_bus_segment = models.ForeignKey(Bus_Segment, null=False, on_delete=models.CASCADE)
