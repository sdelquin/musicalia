from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=256)
    starting_year = models.PositiveSmallIntegerField()
    website = models.URLField(blank=True)

    def __str__(self):
        return self.name
