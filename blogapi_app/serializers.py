from rest_framework import serializers
from .models import Profile, Post, Category, Comment, Favorite


        
class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Profile model.

    This serializer is used to convert Profile model instances
    into JSON format and vice versa.

    Attributes:
        user (serializers.HiddenField): Hidden field that sets
            the user to the currently authenticated user.

    Meta:
        model (Profile): The Profile model class to be serialized.
        fields (tuple): A tuple of field names to be included in
            the serialized representation. Uses '__all__' to include
            all fields of the model.
    """
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model=Profile
        fields='__all__'
        
class PostSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Post model.

    This serializer is used to convert Post model instances
    into JSON format and vice versa.

    Attributes:
        post_author (serializers.HiddenField): Hidden field that sets
            the post_author to the currently authenticated user.

    Meta:
        model (Post): The Post model class to be serialized.
        fields (tuple): A tuple of field names to be included in
            the serialized representation. Uses '__all__' to include
            all fields of the model.
    """
    post_author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model=Post
        fields='__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    """
    Serializer class for the Category model.

    This serializer is used to convert Category model instances
    into JSON format and vice versa.

    Meta:
        model (Category): The Category model class to be serialized.
        fields (tuple): A tuple of field names to be included in
            the serialized representation. Uses '__all__' to include
            all fields of the model.
    """
    class Meta:
        model=Category
        fields='__all__'
        
class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Comment model.

    This serializer is used to convert Comment model instances
    into JSON format and vice versa.

    Meta:
        model (Comment): The Comment model class to be serialized.
        fields (tuple): A tuple of field names to be included in
            the serialized representation. Uses '__all__' to include
            all fields of the model.
    """
    class Meta:
        model=Comment
        fields='__all__'
        
class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer class for the Favorite model.

    This serializer is used to convert Favorite model instances
    into JSON format and vice versa.

    Attributes:
        user (serializers.HiddenField): Hidden field that sets
            the user to the currently authenticated user.

    Meta:
        model (Favorite): The Favorite model class to be serialized.
        fields (tuple): A tuple of field names to be included in
            the serialized representation. Uses '__all__' to include
            all fields of the model.
    """
    
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model=Favorite
        fields='__all__'
        