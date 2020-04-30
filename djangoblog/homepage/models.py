from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0, "Drafted Post"),
    (1, "Publish Post")
)

class Author(models.Model):
    name = models.CharField(max_length=200) #max length is set to 200 to account for longer names
    bio = models.TextField()

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=100) #set this to 100 to help make users more inclined to make their blog titles concise and not too long
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete = models.CASCADE) #if an author were to be deleted, we would want all the posts by that author to be deleted as well
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title