from users.models import Participant,Comment
from rest_framework import generics,mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly
from users.serializers import ParticipantSerializer,CommentsReadSerializer,CommentsSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from users.filters import CommentsFilter



class CommentsViewsSet(mixins.RetrieveModelMixin,mixins.ListModelMixin,GenericViewSet):#Для GET
    serializer_class = CommentsReadSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = CommentsFilter
    permission_classes = (IsAuthenticated, )
    
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if not pk:
            queryset = Comment.objects.all()# [:2]
            return queryset
        else:
            queryset = Comment.objects.filter(pk=pk)
            return queryset
        


class CommentsPostAPIList(generics.ListCreateAPIView):#для POST 
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CommentsAPIUpdate(generics.RetrieveUpdateAPIView):#для PUT
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
 
 
class CommentsAPIDestroy(generics.RetrieveDestroyAPIView):#для DELETE
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class ParticipantViewsSet(mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.ListModelMixin,
                GenericViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer
    


