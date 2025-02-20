from django.urls import path ,include

from rest_framework.routers import DefaultRouter

from apps.book.api.views.book import BookViewSet, CommentViewSet


router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'comments', CommentViewSet)
urlpatterns = [
    path('', include(router.urls)),
]

