from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register('v1/posts', PostViewSet)
v1_router.register(r'v1/posts/(?P<id>[0-9]+)/comments', CommentViewSet)

urlpatterns = v1_router.urls


urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
