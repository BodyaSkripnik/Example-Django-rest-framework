from django.shortcuts import render
from users.models import Participant,Comment
from rest_framework import generics,mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAdminOrReadOnly,IsOwnerOrReadOnly
from rest_framework.response import Response
from users.serializers import ParticipantSerializer,CommentsReadSerializer,CommentsSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response


class CommentsGetAPIList(generics.ListCreateAPIView):#для GET
    queryset = Comment.objects.all()
    serializer_class = CommentsReadSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


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