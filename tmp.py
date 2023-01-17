from django.db import models


class Event(models.Model):
    name = models.CharField(max_length=200)
    start_at = models.DateTimeField()
    description = models.TextField()
    contact = models.EmailField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='events')
    location = models.CharField(max_length=400)
