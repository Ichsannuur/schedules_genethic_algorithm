from django.db import models
from model_utils import Choices


class Schedule(models.Model):
    DAYS = Choices(
        (1, "senin", "Senin"),
        (2, "selasa", "Selasa"),
        (3, "rabu", "Rabu"),
        (4, "kamis", "Kamis"),
        (5, "jumat", "Jumat"),
        (6, "sabtu", "Sabtu"),
        (7, "minggu", "Minggu"),
    )

    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.PositiveSmallIntegerField(choices=DAYS)
    courses = models.ForeignKey("courses.Course", related_name='schedules')
    lectures = models.ForeignKey("lecturers.Lecture", related_name='schedules')
    classrooms = models.ForeignKey("classrooms.Classroom", related_name='schedules')

    def __str__(self):
        return f"{self.classrooms} # {self.start_time} - {self.end_time}"
