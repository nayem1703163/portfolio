from django.contrib import admin
from .models import blog_technology
from .models import UserProfileInfo
# Register your models here.

admin.site.register(blog_technology)
admin.site.register(UserProfileInfo)
