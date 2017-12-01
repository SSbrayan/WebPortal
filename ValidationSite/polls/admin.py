from django.contrib import admin

from .models import Question
from .models import Target
from .models import Interface
from .models import Port

admin.site.register(Question)
admin.site.register(Target)
admin.site.register(Interface)
admin.site.register(Port)