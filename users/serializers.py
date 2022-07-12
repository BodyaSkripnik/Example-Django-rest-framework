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

    class Meta:
        model = Comment
        fields = ('id', 'title', 'created_date','participant','project')


class CommentsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields = ('id', 'title', 'created_date','participant','project')