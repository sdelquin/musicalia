from django.db import models


class Track(models.Model):
    name = models.CharField(max_length=256)
    artist = models.ForeignKey(
        'artists.Artist',
        on_delete=models.CASCADE,
        related_name='tracks',
    )
    length = models.IntegerField()  # in seconds
    num_visits = models.PositiveBigIntegerField(default=0)

    def __str__(self):
        return self.name
