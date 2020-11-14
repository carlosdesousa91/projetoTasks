from django.db import models

class Task(models.Model):
    title = models.TextField(max_length=32, blank=False, null = False)
