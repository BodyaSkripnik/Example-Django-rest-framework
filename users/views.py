from django.shortcuts import render
from users.models import Participant,Comments
from rest_framework import generics,mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly

from users.serializers import ParticipantSerializer,CommentsSerializer


class CommentsAPIList(generics.ListCreateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
 
 
class CommentsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsOwnerOrReadOnly, )
 
 
class CommentsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Comments.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAdminOrReadOnly, )

class ParticipantViewsSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer