from django.contrib import admin
from users.models import Comment,Participant,Role


for model in [Comment,Participant,Role]:
    admin.site.register(model)