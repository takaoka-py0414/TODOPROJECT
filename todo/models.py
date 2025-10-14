from django.db import models

# Create your models here.

CHOICE = (('大','幸福度：大'),('中','幸福度：中'),('小','幸福度：小'))

class TodoModel(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
    )
    duedate = models.DateField()
    def __str__(self):
        return self.title
    
class Meal(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
    )
    duedate = models.DateField()
    category = models.CharField(max_length=20,)
    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
    )
    duedate = models.DateField()
    def __str__(self):
        return self.title