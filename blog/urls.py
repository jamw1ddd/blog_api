from django.urls import path,include
from rest_framework.routers import DefaultRouter

from blog.views import PostViewSet,CategoryViewSet

router = DefaultRouter()
router.register(r'categories',CategoryViewSet,basename='category')
router.register(r'posts',PostViewSet,basename='post')

urlpatterns = [
    path('blog/',include(router.urls)),
]