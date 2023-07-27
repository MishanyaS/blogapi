from django.urls import path, include, re_path
from .views import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView



urlpatterns = [
    # Authentication URLs
    # Example: http://127.0.0.1:8000/api/v1/auth-blogapi/login/login/
    path('api/v1/auth-blogapi/login/', include('rest_framework.urls')),
    
    # Profile URLs
    path(route='api/v1/profile/', view=ProfileAPIList.as_view()),
    path(route='api/v1/profile/<int:pk>/', view=ProfileAPIUpdate.as_view()),
    path(route='api/v1/profiledelete/<int:pk>/', view=ProfileAPIDestroy.as_view()),
    
    # Post URLs
    path(route='api/v1/post/', view=PostAPIList.as_view()),
    path(route='api/v1/post/<int:pk>/', view=PostAPIUpdate.as_view()),
    path(route='api/v1/postdelete/<int:pk>/', view=PostAPIDestroy.as_view()),
    
     # Category URLs
    path(route='api/v1/category/', view=CategoryAPIList.as_view()),
    path(route='api/v1/category/<int:pk>/', view=CategoryAPIUpdate.as_view()),
    path(route='api/v1/categorydelete/<int:pk>/', view=CategoryAPIDestroy.as_view()),
    
    # Comment URLs
    path(route='api/v1/comment/', view=CommentAPIList.as_view()),
    path(route='api/v1/comment/<int:pk>/', view=CommentAPIUpdate.as_view()),
    path(route='api/v1/commentdelete/<int:pk>/', view=CommentAPIDestroy.as_view()),
    
    # Favorite URLs
    path(route='api/v1/favorite/', view=FavoriteAPIList.as_view()),
    path(route='api/v1/favorite/<int:pk>/', view=FavoriteAPIUpdate.as_view()),
    path(route='api/v1/favoritedelete/<int:pk>/', view=FavoriteAPIDestroy.as_view()),
    
    # Auth URLs
    path('api/v1/auth/', include('djoser.urls')),
    # Example: http://127.0.0.1:8000/auth/token/login/
    re_path(r'^auth/', include('djoser.urls.authtoken')),
    
    # JWT token URLs
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]