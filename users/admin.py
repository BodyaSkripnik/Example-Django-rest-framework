from django.contrib import admin
from users.models import Comments,Participant


for model in [Comments,Participant]:
    admin.site.register(model)