from django.contrib import admin
from users.models import Comment,Participant


for model in [Comment,Participant]:
    admin.site.register(model)