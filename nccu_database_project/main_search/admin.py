from django.contrib import admin
from .models import User, Location, Bank, Record, Company, Type, Commodity, State
# Register your models here.
admin.site.register(User)
admin.site.register(Location)
admin.site.register(Bank)
admin.site.register(Record)
admin.site.register(Company)
admin.site.register(Type)
admin.site.register(Commodity)
admin.site.register(State)
