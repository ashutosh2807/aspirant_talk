from django.contrib import admin
from .models import *

admin.site.register(Category)
admin.site.register(Sub_category)
admin.site.register(Comment)
admin.site.register(Blog)