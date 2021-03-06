from django.db import models

__all__ = (
    "City",
)


class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Город')

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ('name',)

    def __str__(self):
        return self.name
