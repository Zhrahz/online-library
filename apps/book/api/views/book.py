
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError, PermissionDenied
from rest_framework.permissions import AllowAny
from rest_framework.decorators import action
from rest_framework.response import Response


from django_filters.rest_framework import DjangoFilterBackend

from apps.book.permissions import IsAdminUser
from apps.book.api.filters.book import BookFilter
from apps.book.models import Book, Comment
from apps.book.api.serializers.book import BookSerializer, CommentSerializer



class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filterset_fields = ['title', 'author']
    filter_backends = [DjangoFilterBackend]
    filterset_class = BookFilter
def get_permissions(self):
        if self.request.method in ['POST', 'DELETE', 'PUT', 'PATCH']:
            return [IsAdminUser()]
        return [AllowAny()]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_object(self):
        user = self.request.user
        obj = super().get_object()
        if obj.user != user:
            raise PermissionDenied("شما اجازه دسترسی به این کامنت را ندارید.")
        return obj

    def get_permissions(self):
        if self.request.method in ['PUT', 'PATCH'] and self.request.user.role != "user":
            raise ValidationError("")
        return super().get_permissions()

    # def perform_create(self, serializer):
    #     user = self.request.user
    #     if not user.is_authenticated:
    #         raise ValidationError('You must be logged in')
    #
    #     super().perform_create(serializer)


    @action(detail=True, methods=['post'], permission_classes=[IsAdminUser])
    def confirm(self, request, pk=None):
        comment = self.get_object()
        comment.is_confirmed = True
        comment.save()
        return Response(self.serializer_class(comment), status=status.HTTP_200_OK)


