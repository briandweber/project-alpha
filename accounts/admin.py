from django.contrib import admin
from accounts.models import Profile

# Register your models here.
admin.site.register(Profile)

class Profile(admin.ModelAdmin):
    list_display = [
        "user",
        "avatar",
        "bio",
    ]
