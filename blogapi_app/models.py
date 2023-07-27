from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    """
    A model representing a user profile.
    
    Inherits from Model.
    
    Attributes:
        user (User): One-to-one relationship with the built-in Django User model, representing the associated user for this profile.
        user_photo (ImageField): An ImageField that stores the user's photo. It allows null and blank values and defines an upload path for the image files.
        user_description (TextField): A TextField that stores the user's description. It allows null and blank values.
        registration_date (DateTimeField): A DateTimeField that stores the registration date of the profile. It is automatically set to the current date and time when the profile is created.
        phone (CharField): A CharField that stores the user's phone number. It allows a maximum length of 10 characters and allows null and blank values.
        user_link (CharField):  A CharField that stores a link associated with the user. It allows a maximum length of 200 characters and allows null and blank values.
        user_birth_date (DateField): A DateField that stores the user's birth date. It allows null and blank values.
        user_github_url (CharField): A CharField that stores the user's GitHub URL. It allows a maximum length of 200 characters and allows null and blank values.
        
    Meta:
        verbose_name (str): The singular name of the profile.
        verbose_name_plural (str): The plural name of the profile.

    Methods:
        __str__(): Returns the string representation of the profile.
        get_absolute_url(): Returns the absolute URL of the profile.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=False, blank=False)
    user_photo = models.ImageField(null=True, blank=True, upload_to='images/profile/')
    user_description = models.TextField(null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    user_link = models.CharField(max_length=200, null=True, blank=True)
    user_birth_date = models.DateField(null=True, blank=True)
    user_github_url = models.CharField(max_length=200, null=True, blank=True)
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

class Post(models.Model):
    """
    Represents a post.
    
    Inherits from Model.

    Attributes:
        post_title (CharField): The title of the post.
        post_image (ImageField): The image associated with the post.
        post_content (RichTextField): The content of the post.
        post_category (CharField): The category of the post.
        post_date (DateTimeField): The date the post was created.
        post_author (ForeignKey): The author of the post.
        favorites (ManyToManyField): Users who have favorited the post.
        likes (ManyToManyField): Users who have liked the post.
        
    Meta:
        ordering (list[str]): Default ordering of instances based on the primary key.
        verbose_name (str): The singular name of the post.
        verbose_name_plural (str): The plural name of the post.
        unique_together (tuple): Fields must be unique together.

    Methods:
        total_likes(): Returns the total number of likes for the post.
        increase_likes(): Increases the number of likes for the post by 1.
        decrease_likes(): Decreases the number of likes for the post by 1, if the current count is greater than 0.
        total_posts(): Returns the total number of posts.
        __str__(): Returns the string representation of the post.
        get_absolute_url(): Returns the absolute URL of the post.
    """
    post_title = models.CharField(max_length=200, null=False, blank=False)
    post_image = models.ImageField(null=True, blank=True, upload_to='images/posts')
    post_content = models.TextField(null=False, blank=False, default="Post content")
    post_category = models.CharField(max_length=200, default='programming')
    post_date = models.DateTimeField(auto_now_add=True)
    post_author = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    favorites = models.ManyToManyField(User, through='Favorite', related_name='favorite_posts')
    likes = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        ordering = ['-pk']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        unique_together = ('post_title', 'post_content')
        
class Category(models.Model):
    """
    Represents a category.
    
    Inherits from Model.

    Attributes:
        name (str): The name of the category.
        description (RichTextField): The description of the category.
        icon (ImageField): An image representing the category.
        svg_icon (FileField): An SVG file representing the category.

    Meta:
        verbose_name (str): The singular name of the category.
        verbose_name_plural (str): The plural name of the category.

    Methods:
        __str__(): Returns the string representation of the category.
        get_absolute_url(): Returns the absolute URL of the category.
    """
    name = models.CharField(max_length=30, null=False, blank=False)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='category_icons/', blank=True, null=True)
    svg_icon = models.FileField(upload_to='category_icons/', blank=True, null=True)
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
class Comment(models.Model):
    """
    Represents a comment on a post.
    
    Inherits from Model.

    Attributes:
        post (ForeignKey): The post that the comment belongs to.
        name (CharField): The name of the commenter.
        comment_content (RichTextField): The content of the comment.
        comment_date (DateTimeField): The date and time when the comment was made.

    Meta:
        verbose_name (str): The singular name of the comment.
        verbose_name_plural (str): The plural name of the comment.

    Methods:
        __str__(): Returns the string representation of the comment.
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    comment_content = models.TextField(null=False, blank=False, default="Comment")
    comment_date = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        
class Favorite(models.Model):
    """
    Represents a favorite relationship between a user and a post.
    
    Inherits from Model.

    Attributes:
        post (ForeignKey): The post that is being favorited.
        user (ForeignKey): The user who favorited the post.
        created_at (DateTimeField): The date and time when the favorite relationship was created.

    Meta:
        verbose_name (str): The singular name of the favorite relationship.
        verbose_name_plural (str): The plural name of the favorite relationship.
        unique_together (tuple): Specifies that the combination of 'post' and 'user' should be unique.
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        """
        In Django, the Meta class is a commonly used inner class that allows you to define metadata for a model class.
        """
        verbose_name = 'Favorite'
        verbose_name_plural = 'Favorites'
        unique_together = ('post', 'user')
        
