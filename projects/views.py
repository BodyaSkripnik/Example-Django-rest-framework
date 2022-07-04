from django.shortcuts import render
from projects.models import Project
from projects.serializers import ProjectSerializer
from rest_framework import generics,viewsets,mixins
from rest_framework.viewsets import GenericViewSet




class ProjectViewsSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


