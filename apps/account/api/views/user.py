from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from apps.account.models import User
from apps.account.api.serializers.user import UserSerializer, UserListSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "User created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListView(APIView):
    pagination_class = PageNumberPagination

    def get(self, request):
        if request.user.role == 'admin':
            users = User.objects.all()
        else:
            users = User.objects.filter(id=request.user.id)

        paginator = self.pagination_class()
        paginated_users = paginator.paginate_queryset(users, request)

        serializer = UserListSerializer(paginated_users, many=True)
        return paginator.get_paginated_response(serializer.data)