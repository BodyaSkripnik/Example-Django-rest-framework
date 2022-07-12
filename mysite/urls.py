from django.contrib import admin
from django.urls import path,include
from projects.views import ProjectViewsSet
from rest_framework import routers
from users.views import ParticipantViewsSet,CommentsPostAPIList,CommentsViewsSet,CommentsAPIUpdate,CommentsAPIDestroy
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)


router = routers.SimpleRouter()
router.register(r'project',ProjectViewsSet)
router.register(r'participant',ParticipantViewsSet)
# router.register(r'comments/get',CommentsViewsSet)
router.register(r'comments/get', CommentsViewsSet, basename='comments')

urlpatterns = router.urls + [
    path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls)),
    # path('api/v1/comments/get/', CommentsGetAPIList.as_view()),
    # path('api/v1/comments/get/<str:pk>/', CommentsGetAPIList.as_view()),
    path('api/v1/comments/post/', CommentsPostAPIList.as_view()),
    path('api/v1/comments/update/<str:pk>/', CommentsAPIUpdate.as_view()),
    path('api/v1/comments/delete/<str:pk>/', CommentsAPIDestroy.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]