from django.db import models

#To create Author Model
class Author(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name

#To Create Book Model
class Book(models.Model):
    name=models.CharField(max_length=200)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name="books")
    created_at=models.DateTimeField(auto_now_add=True)
    last_edited=models.DateTimeField(auto_now=True)
    description=models.TextField()
    def __str__(self):
        return self.name
