from django.contrib import admin

from recommendation.models import UserProfile, Lawyer

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Lawyer)