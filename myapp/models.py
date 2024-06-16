from django.db import models
from django.contrib.auth.models import User

class Music(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='music/')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)  # Manually specify the default value

    def __str__(self):
        return self.title

class MyModel(models.Model):
    """
    A simple model example with a single field.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        """
        Return a string representation of the model.
        """
        return self.name