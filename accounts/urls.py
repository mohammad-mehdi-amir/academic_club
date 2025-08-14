from django.urls import path
from .views import RegisterView, ProfileView, UserDetailView,api_docs
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', api_docs, name='home'),
    path('register/', RegisterView.as_view(), name='auth-register'),
    path('token/', TokenObtainPairView.as_view(), name='token-obtain-pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token-refresh'),
    path('me/profile/', ProfileView.as_view(), name='my-profile'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]