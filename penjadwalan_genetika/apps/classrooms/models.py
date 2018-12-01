from django.db import models


class Classroom(models.Model):
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('name', )

    def __str__(self):
        return self.name
