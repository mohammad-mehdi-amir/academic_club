from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignupView
from django.urls import path,include



urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # login
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignupView.as_view(), name='signup'),
]

