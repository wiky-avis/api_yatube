from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register(r'posts/(?P<id>[0-9]+)/comments', CommentViewSet)

urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token),
]
