from django.contrib import admin
from covit.models import *

# Register your models here.

admin.site.register(Route)
admin.site.register(Bus)
admin.site.register(Stop)
admin.site.register(Segment)
admin.site.register(Bus_Segment)
admin.site.register(Person)
admin.site.register(Direction)