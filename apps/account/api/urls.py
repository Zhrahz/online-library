from django.urls import path

from apps.account.api.views.user import RegisterView , UserListView

from rest_framework_simplejwt.views import TokenObtainPairView,  TokenRefreshView



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('userlist/',UserListView.as_view(), name='user-list'),

]