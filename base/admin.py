from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Matter),
admin.site.register(Task),
admin.site.register(Event),
admin.site.register(IndividualClient),
admin.site.register(BusinessClient),
admin.site.register(Lawyer),
admin.site.register(Note),
admin.site.register(Document),

