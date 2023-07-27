from rest_framework import generics
from blogapi_app.serializers import CategorySerializer, CommentSerializer, FavoriteSerializer, PostSerializer, ProfileSerializer
from .models import Profile, Post, Category, Comment, Favorite

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnlyForProfile, IsOwnerOrReadOnlyForPost, IsOwnerOrReadOnlyForFavorite
from rest_framework.pagination import PageNumberPagination

# Create your views here.

class ProfileAPIListPagination(PageNumberPagination):
    """
    Pagination class for the Profile list API.

    This class specifies the pagination behavior for the ProfileAPIList view.

    Attributes:
        page_size (int): The number of profiles to include on each page.
        page_size_query_param (str): The name of the query parameter
            that controls the page size.
        max_page_size (int): The maximum allowed page size.
    """
    page_size=3
    page_size_query_param='page_size'
    max_page_size=100

class ProfileAPIList(generics.ListCreateAPIView):
    """
    API view for listing and creating profiles.

    This view provides endpoints for retrieving a list of profiles
    and creating new profiles.

    Attributes:
        queryset (QuerySet): The queryset of Profile objects to be used.
        serializer_class (Serializer): The serializer class for Profile objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
        pagination_class (Pagination): The pagination class to be used
            for this view.
    """
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=(IsAuthenticatedOrReadOnly, )
    pagination_class=ProfileAPIListPagination
    
class ProfileAPIUpdate(generics.RetrieveUpdateAPIView):
    """
    API view for retrieving and updating a profile.

    This view provides endpoints for retrieving and updating a specific profile.

    Attributes:
        queryset (QuerySet): The queryset of Profile objects to be used.
        serializer_class (Serializer): The serializer class for Profile objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
    """
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=(IsOwnerOrReadOnlyForProfile, )
    
class ProfileAPIDestroy(generics.RetrieveDestroyAPIView):
    """
    API view for retrieving and deleting a profile.

    This view provides endpoints for retrieving and deleting a specific profile.

    Attributes:
        queryset (QuerySet): The queryset of Profile objects to be used.
        serializer_class (Serializer): The serializer class for Profile objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
    """
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=(IsOwnerOrReadOnlyForProfile, )



class PostAPIListPagination(PageNumberPagination):
    """
    Pagination class for the Post list API.

    This class specifies the pagination behavior for the PostAPIList view.

    Attributes:
        page_size (int): The number of posts to include on each page.
        page_size_query_param (str): The name of the query parameter
            that controls the page size.
        max_page_size (int): The maximum allowed page size.
    """
    page_size=3
    page_size_query_param='page_size'
    max_page_size=100

class PostAPIList(generics.ListCreateAPIView):
    """
    API view for listing and creating posts.

    This view provides endpoints for retrieving a list of posts
    and creating new posts.

    Attributes:
        queryset (QuerySet): The queryset of Profile objects to be used.
        serializer_class (Serializer): The serializer class for Profile objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
        pagination_class (Pagination): The pagination class to be used
            for this view.
    """
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=(IsAuthenticatedOrReadOnly, )
    pagination_class=PostAPIListPagination
    
class PostAPIUpdate(generics.RetrieveUpdateAPIView):
    """
    API view for retrieving and updating a post.

    This view provides endpoints for retrieving and updating a specific post.

    Attributes:
        queryset (QuerySet): The queryset of Post objects to be used.
        serializer_class (Serializer): The serializer class for Post objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
    """
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=(IsOwnerOrReadOnlyForPost, )
    
class PostAPIDestroy(generics.RetrieveDestroyAPIView):
    """
    API view for retrieving and deleting a post.

    This view provides endpoints for retrieving and deleting a specific post.

    Attributes:
        queryset (QuerySet): The queryset of Post objects to be used.
        serializer_class (Serializer): The serializer class for Post objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
    """
    queryset=Post.objects.all()
    serializer_class=PostSerializer
    permission_classes=(IsOwnerOrReadOnlyForPost, )
    
    

class CategoryAPIListPagination(PageNumberPagination):
    """
    Pagination class for the Category list API.

    This class specifies the pagination behavior for the CategoryAPIList view.

    Attributes:
        page_size (int): The number of categories to include on each page.
        page_size_query_param (str): The name of the query parameter
            that controls the page size.
        max_page_size (int): The maximum allowed page size.
    """
    page_size=3
    page_size_query_param='page_size'
    max_page_size=100

class CategoryAPIList(generics.ListCreateAPIView):
    """
    API view for listing and creating categories.

    This view provides endpoints for retrieving a list of categories
    and creating new categories.

    Attributes:
        queryset (QuerySet): The queryset of Profile objects to be used.
        serializer_class (Serializer): The serializer class for Profile objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
        pagination_class (Pagination): The pagination class to be used
            for this view.
    """
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsAdminOrReadOnly,)
    pagination_class=CategoryAPIListPagination
    
class CategoryAPIUpdate(generics.RetrieveUpdateAPIView):
    """
    API view for retrieving and updating a category.

    This view provides endpoints for retrieving and updating a specific category.

    Attributes:
        queryset (QuerySet): The queryset of Category objects to be used.
        serializer_class (Serializer): The serializer class for Category objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
    """
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsAdminOrReadOnly, )
    
class CategoryAPIDestroy(generics.RetrieveDestroyAPIView):
    """
    API view for retrieving and deleting a category.

    This view provides endpoints for retrieving and deleting a specific category.

    Attributes:
        queryset (QuerySet): The queryset of Category objects to be used.
        serializer_class (Serializer): The serializer class for Category objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
    """
    queryset=Category.objects.all()
    serializer_class=CategorySerializer
    permission_classes=(IsAdminOrReadOnly, )
    
    

class CommentAPIListPagination(PageNumberPagination):
    """
    Pagination class for the Comment list API.

    This class specifies the pagination behavior for the CommentAPIList view.

    Attributes:
        page_size (int): The number of comments to include on each page.
        page_size_query_param (str): The name of the query parameter
            that controls the page size.
        max_page_size (int): The maximum allowed page size.
    """
    page_size=3
    page_size_query_param='page_size'
    max_page_size=100

class CommentAPIList(generics.ListCreateAPIView):
    """
    API view for listing and creating comments.

    This view provides endpoints for retrieving a list of comments
    and creating new comments.

    Attributes:
        queryset (QuerySet): The queryset of Profile objects to be used.
        serializer_class (Serializer): The serializer class for Profile objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
        pagination_class (Pagination): The pagination class to be used
            for this view.
    """
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=(IsAuthenticatedOrReadOnly, )
    pagination_class=CommentAPIListPagination
    
class CommentAPIUpdate(generics.RetrieveUpdateAPIView):
    """
    API view for retrieving and updating a comment.

    This view provides endpoints for retrieving and updating a specific comment.

    Attributes:
        queryset (QuerySet): The queryset of Comment objects to be used.
        serializer_class (Serializer): The serializer class for Comment objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
    """
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=(IsAdminUser, )
    
class CommentAPIDestroy(generics.RetrieveDestroyAPIView):
    """
    API view for retrieving and deleting a comment.

    This view provides endpoints for retrieving and deleting a specific comment.

    Attributes:
        queryset (QuerySet): The queryset of Comment objects to be used.
        serializer_class (Serializer): The serializer class for Comment objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
    """
    queryset=Comment.objects.all()
    serializer_class=CommentSerializer
    permission_classes=(IsAdminUser, )
    
    

class FavoriteAPIListPagination(PageNumberPagination):
    """
    Pagination class for the Favorite list API.

    This class specifies the pagination behavior for the FavoriteAPIList view.

    Attributes:
        page_size (int): The number of favorites to include on each page.
        page_size_query_param (str): The name of the query parameter
            that controls the page size.
        max_page_size (int): The maximum allowed page size.
    """
    page_size=3
    page_size_query_param='page_size'
    max_page_size=100

class FavoriteAPIList(generics.ListCreateAPIView):
    """
    API view for listing and creating favorites.

    This view provides endpoints for retrieving a list of favorites
    and creating new favorites.

    Attributes:
        queryset (QuerySet): The queryset of Profile objects to be used.
        serializer_class (Serializer): The serializer class for Profile objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
        pagination_class (Pagination): The pagination class to be used
            for this view.
    """
    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer
    permission_classes=(IsAuthenticatedOrReadOnly, )
    pagination_class=FavoriteAPIListPagination
    
class FavoriteAPIUpdate(generics.RetrieveUpdateAPIView):
    """
    API view for retrieving and updating a favorite.

    This view provides endpoints for retrieving and updating a specific favorite.

    Attributes:
        queryset (QuerySet): The queryset of Favorite objects to be used.
        serializer_class (Serializer): The serializer class for Favorite objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
    """
    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer
    permission_classes=(IsOwnerOrReadOnlyForFavorite, )
    
class FavoriteAPIDestroy(generics.RetrieveDestroyAPIView):
    """
    API view for retrieving and deleting a favorite.

    This view provides endpoints for retrieving and deleting a specific favorite.

    Attributes:
        queryset (QuerySet): The queryset of Favorite objects to be used.
        serializer_class (Serializer): The serializer class for Favorite objects.
        permission_classes (tuple): The permission classes to be applied
            for this view.
    """
    queryset=Favorite.objects.all()
    serializer_class=FavoriteSerializer
    permission_classes=(IsOwnerOrReadOnlyForFavorite, )
