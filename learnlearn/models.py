from django.db import models
from django.db.models import ForeignKey


class Lector(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_started = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.id} {self.full_name}'


class Course(models.Model):
    CATEGORIES = ((1, 'Python'), (2, 'C++'), )
    name = models.CharField(max_length=150)
    category = models.IntegerField(choices= CATEGORIES, default=1)
    description = models.TextField(default=None)
    date_started = models.DateTimeField(auto_now_add=True)

    lector = ForeignKey(Lector, models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.name}'


class Lesson(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(default=None)
    date_start = models.DateTimeField(auto_now_add=True)

    course = ForeignKey(Course, models.CASCADE)

    def __str__(self):
        return f'{self.id} {self.name}'
