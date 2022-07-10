from django.shortcuts import render
from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework import generics,viewsets,mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin
from users.models import Comment




class ProjectViewsSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

    # def get_queryset(self, pk=None):
    #     if pk is not None:
    #         pk = Comment.objects.get(participant_id=pk)
    #         pk = Project.filter(id=pk)
    #         return queryset
    #     else:
    #         queryset = Project.objects.all()
    #         return queryset


