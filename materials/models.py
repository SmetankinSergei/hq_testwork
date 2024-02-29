from django.db import models
from django.db.models import CASCADE

from users.models import User


class Material(models.Model):
    author = models.CharField(max_length=250)
    name = models.CharField(max_length=500)
    start_time = models.DateTimeField()
    price = models.PositiveIntegerField(default=0)
    min_students_in_group = models.PositiveIntegerField()
    max_students_in_group = models.PositiveIntegerField()
    material_users = models.ManyToManyField(to=User, related_name='material_users')

    def __str__(self):
        return self.name


class Lesson(models.Model):
    name = models.CharField(max_length=500)
    video_url = models.URLField()
    material = models.ForeignKey(to=Material, on_delete=CASCADE, related_name='lessons')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=250)
    students = models.ManyToManyField(to=User, related_name='students')
    material = models.ForeignKey(to=Material, on_delete=CASCADE, related_name='material_groups')

    def __str__(self):
        return self.name
