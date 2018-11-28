from django.db import models
from model_utils import Choices


class Course(models.Model):

    TYPE = Choices(
        (1, "teori", "Teori"),
        (2, "praktik", "Praktik")
    )

    name = models.CharField(max_length=50)
    sks = models.IntegerField()
    semester = models.IntegerField()
    isActive = models.BooleanField(default=True)
    type = models.PositiveSmallIntegerField(choices=TYPE, default=TYPE.teori)

    def __str__(self):
        return self.name
