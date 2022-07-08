
from django.contrib import admin
from django.urls import path,include
from projects.views import ProjectViewsSet
from rest_framework import routers
from users.views import ParticipantViewsSet,CommentsAPIDestroy,CommentsAPIUpdate,CommentsGetAPIList,CommentsPostAPIList
from users.views import CustomAuthToken


router = routers.SimpleRouter()
router.register(r'project',ProjectViewsSet)
router.register(r'participant',ParticipantViewsSet)
print(router.urls)


urlpatterns = router.urls + [
    path('admin/', admin.site.urls),
    path('api/v1/',include(router.urls)),
    path('api/v1/comments/get/', CommentsGetAPIList.as_view()),
    path('api/v1/comments/get/<str:pk>/', CommentsGetAPIList.as_view()),
    path('api/v1/comments/post/', CommentsPostAPIList.as_view()),
    path('api/v1/comments/update/<str:pk>/', CommentsAPIUpdate.as_view()),
    path('api/v1/comments/delete/<str:pk>/', CommentsAPIDestroy.as_view()),
    path('api/token/auth/', CustomAuthToken.as_view())
]
