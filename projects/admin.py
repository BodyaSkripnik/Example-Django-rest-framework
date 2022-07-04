from django.contrib import admin
from projects.models import Project


for model in [Project]:
    admin.site.register(model)

# Register your models here.
