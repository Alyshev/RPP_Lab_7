from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(City)
admin.site.register(Age)
admin.site.register(WorkExperience)
admin.site.register(FullName)
admin.site.register(Position)

