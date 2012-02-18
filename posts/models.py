from django.db import models

class Post(models.Model):
    body=models.TextField(max_length=500, verbose_name='posts body')

