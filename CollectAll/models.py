from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns
from django.contrib.auth.models import User
from datetime import date


class CollectionType(models.Model):
    """Model representing a collection type."""
    collection_type = models.CharField(max_length=25, help_text='Enter a collection type (e.g. sport, music, etc.)')

    def __str__(self):
        """String for representing the Model object."""
        return self.collection_type


class Collection(models.Model):
    """Model representing a Collection."""
    collection_id = models.CharField(max_length=25)
    name = models.CharField(max_length=100)
    public_privacy = models.BooleanField
    collection_favorite = models.CharField(max_length=10)
    collection_image = models.ImageField(upload_to='images/', null=True, blank=True)
    collection_notes = models.TextField(max_length=1000)

    def get_absolute_url(self):
        """Returns the URL to access a particular collection instance."""
        return reverse('collection_notes', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.name}'


class CollectionItem(models.Model):
    """Model representing a collection item."""
    item_name = models.CharField(max_length=200)
    # Foreign Key used because CollectionItems can only have one collection, but collections can have multiple items
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='collection_items')
    collection_type_id = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='collection_type_items')
    parent_collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name='child_items')
    item_notes = models.TextField(max_length=1000, help_text='Enter a brief description of the item')
    unique_id = models.IntegerField
    item_rank = models.IntegerField
    item_value = models.DecimalField(max_digits=10, decimal_places=2)
    collected_date = models.DateField()
    item_image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.collection_id

    def get_absolute_url(self):
        """Returns the URL to access a detail record for this item."""
        return reverse('item_notes', args=[str(self.id)])


class UserProfile(models.Model):
    """Model representing a specific user"""
    user_id = models.CharField(max_length=15)
    admin = models.BooleanField
    user_image = models.ImageField(upload_to='images/', null=True, blank=True)
    profile_privacy = models.BooleanField
    user_email = models.CharField(max_length=30)
    user_password = models.CharField
    user_description = models.TextField(max_length=1000)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.id} ({self.user_id.title})'


class UserComment(models.Model):
    user_comment_id = models.IntegerField
    user_id = models.ForeignKey(UserProfile, on_delete=models.RESTRICT, null=True)
    collection_id = models.ForeignKey(Collection, on_delete=models.RESTRICT, null=True)
    user_comment = models.TextField(max_length=1000)
# Create your models here.
