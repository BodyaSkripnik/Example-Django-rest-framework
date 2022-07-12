from rest_framework import serializers
from projects.models import Project
# from users.serializers import CommentsReadSerializer


class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = ['id','created_date','name','photo']

        
        
        