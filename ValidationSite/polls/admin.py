from django.contrib import admin

from .models import Question
from .models import Target

admin.site.register(Question)
admin.site.register(Target)