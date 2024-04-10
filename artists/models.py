from django.db import models


class Artist(models.Model):
    class Scope(models.TextChoices):
        LOCAL = 'L', 'Local'
        NATIONAL = 'N', 'Nacional'
        INTERNATIONAL = 'I', 'Internacional'

    name = models.CharField(max_length=256)
    starting_year = models.PositiveSmallIntegerField()
    website = models.URLField(blank=True)
    scope = models.CharField(
        max_length=1,
        choices=Scope,
        default=Scope.INTERNATIONAL,
    )

    def __str__(self):
        return self.name
