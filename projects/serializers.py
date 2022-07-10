from rest_framework import serializers
from projects.models import Project
# from users.serializers import CommentsReadSerializer


class ProjectSerializer(serializers.ModelSerializer):
    # project = serializers.StringRelatedField(many=True)
    # project = CommentsReadSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ['id','created_date','name','photo']

        
        
        