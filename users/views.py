from django.shortcuts import render
from users.models import Participant,Comment
from rest_framework import generics,mixins,status
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly
from rest_framework.response import Response
from users.serializers import ParticipantSerializer,CommentsReadSerializer,CommentsSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters import rest_framework as filters
from users.filters import CommentsFilter



class CommentsViewsSet(mixins.RetrieveModelMixin,mixins.ListModelMixin,GenericViewSet):
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


class CommentsAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    permission_classes = (IsOwnerOrReadOnly, )
 
 
class CommentsAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Comment.objects.all()
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
    


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })