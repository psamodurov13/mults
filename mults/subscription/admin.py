from django.contrib import admin
from .models import Subscription


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'date')


admin.site.register(Subscription, SubscriptionAdmin)


