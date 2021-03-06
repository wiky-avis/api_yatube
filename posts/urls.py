from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register('posts', PostViewSet)
v1_router.register(
    r'posts/(?P<id>[0-9]+)/comments', CommentViewSet, basename='comments')

urlpatterns = v1_router.urls


urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
