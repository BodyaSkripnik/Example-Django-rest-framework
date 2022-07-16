from rest_framework import serializers
from users.models import Participant,Comment
from projects.serializers import ProjectSerializer

class ParticipantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Participant
        fields = ('id', 'created_date', 'name','photo')


class CommentsReadSerializer(serializers.ModelSerializer):
    
    project = ProjectSerializer(read_only=True,many=False)
    participant = ParticipantSerializer(read_only=True,many=False)
    rating = serializers.CharField(source='get_rating')

    class Meta:
        model = Comment
        fields = ('id', 'title', 'created_date',\
            'participant','project',\
            'project_management_level', 'quality_of_performance', \
            'timeliness_of_performance','culture_and_speed_of_communication',\
            'speed_and_quality_of_defect_elimination','rating')


class CommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'title', 'created_date','participant','project')