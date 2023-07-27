from django.contrib import admin
from .models import Profile, Post, Category, Comment, Favorite

# Register your models here.
admin.site.register(Profile)
"""
Registers the Profile model with the Django admin site.

This allows the Profile model to be managed and displayed
in the Django administration interface.
"""

admin.site.register(Post)
"""
Registers the Post model with the Django admin site.

This allows the Post model to be managed and displayed
in the Django administration interface.
"""

admin.site.register(Category)
"""
Registers the Category model with the Django admin site.

This allows the Category model to be managed and displayed
in the Django administration interface.
"""

admin.site.register(Comment)
"""
Registers the Comment model with the Django admin site.

This allows the Comment model to be managed and displayed
in the Django administration interface.
"""

admin.site.register(Favorite)
"""
Registers the Favorite model with the Django admin site.

This allows the Favorite model to be managed and displayed
in the Django administration interface.
"""