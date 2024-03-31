from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=256)
    singer = models.CharField(max_length=256)
    length = models.IntegerField()  # in seconds

    def __str__(self):
        return self.name
