from django.contrib import admin

from .models import Blog
from .models import Blog2

# Register your models here.
admin.site.register(Blog)
admin.site.register(Blog2)
