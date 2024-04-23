from django.db import models

# Create your models here.

class TodoList(models.Model):
	todo = models.CharField(max_length=100)