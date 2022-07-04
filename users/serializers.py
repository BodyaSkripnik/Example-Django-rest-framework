from rest_framework import serializers
from django.utils.text import slugify
from users.models import Participant,Comments
from projects.serializers import ProjectSerializer


class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participant
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):

    project = ProjectSerializer(read_only=True,many=False)
    participant = ParticipantSerializer(read_only=True,many=False)
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Comments
        fields = ('id', 'title', 'created_date','user','project','participant')