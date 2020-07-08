from django.contrib import admin
from .models import *


class SubscriberAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Subscriber._meta.fields]
# {{{ ._meta.fields }}} - Достаёт все поля, которые есть в Subscriber (итератор)
    list_filter = ['name',]
    search_fields = ['name', 'email']
    fields = ["email"]

    class Meta:
        model = Subscriber

admin.site.register(Subscriber, SubscriberAdmin)