from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Permission class that allows read-only access to non-admin users,
    but only allows write access to administrators.

    Attributes:
        message (str): The error message to be displayed when access is denied.
    """
    def has_permission(self, request, view):
        """
        Check if the user has permission to perform the requested action.

        Args:
            request (HttpRequest): The incoming request.
            view (APIView): The current API view.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return bool(request.user and request.user.is_staff)
    
class IsOwnerOrReadOnlyForProfile(permissions.BasePermission):
    """
    Permission class that allows read-only access to all users,
    but only allows write access to the owner of the profile.

    Attributes:
        message (str): The error message to be displayed when access is denied.
    """
    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to perform the requested action on the profile.

        Args:
            request (HttpRequest): The incoming request.
            view (APIView): The current API view.
            obj (Profile): The profile object being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user
    
class IsOwnerOrReadOnlyForPost(permissions.BasePermission):
    """
    Permission class that allows read-only access to all users,
    but only allows write access to the author of the post.

    Attributes:
        message (str): The error message to be displayed when access is denied.
    """
    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to perform the requested action on the post.

        Args:
            request (HttpRequest): The incoming request.
            view (APIView): The current API view.
            obj (Post): The post object being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.post_author == request.user
    
class IsOwnerOrReadOnlyForComment(permissions.BasePermission):
    """
    Permission class that allows read-only access to all users,
    but only allows write access to the owner of the comment.

    Attributes:
        message (str): The error message to be displayed when access is denied.
    """
    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to perform the requested action on the comment.

        Args:
            request (HttpRequest): The incoming request.
            view (APIView): The current API view.
            obj (Comment): The comment object being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.name == request.user
    
class IsOwnerOrReadOnlyForFavorite(permissions.BasePermission):
    """
    Permission class that allows read-only access to all users,
    but only allows write access to the owner of the favorite.

    Attributes:
        message (str): The error message to be displayed when access is denied.
    """
    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to perform the requested action on the favorite.

        Args:
            request (HttpRequest): The incoming request.
            view (APIView): The current API view.
            obj (Favorite): The favorite object being accessed.

        Returns:
            bool: True if the user has permission, False otherwise.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user == request.user