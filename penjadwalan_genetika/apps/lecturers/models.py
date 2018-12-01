from django.db import models


class Lecture(models.Model):
    name = models.CharField(max_length=50)
    study_programs = models.ForeignKey("study_programs.StudyPrograms", related_name='lectures')
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('name', 'study_programs')

    def __str__(self):
        return self.name
