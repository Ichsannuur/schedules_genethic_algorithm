from django.db import models


class StudyPrograms(models.Model):
    name = models.CharField(max_length=25)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('name',)

    def __str__(self):
        return self.name
