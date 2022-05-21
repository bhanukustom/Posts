from django.contrib import admin
from django.contrib.sessions.models import Session

# Register your models here.

from .models import Posts, Comments


admin.site.register(Posts)
admin.site.register(Comments)
admin.site.register(Session)
