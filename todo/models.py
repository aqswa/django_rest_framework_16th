from django.db import models
from account.models import User


# Create your models here.

class Goal(models.Model):
    PRIVACY_CHOICES = (
        ('숨기기', '숨기기'),
        ('나만보기', '나만보기'),
        ('일부공개', '일부공개'),
        ('전체공개', '전체공개')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='나만보기')
    color = models.CharField(max_length=20)

    def __str__(self):
        return "goal: " + self.title


class Todo(models.Model):
    goal = models.ForeignKey('Goal', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=True)
    date = models.DateField()
    is_done = models.BooleanField()
    is_active = models.BooleanField(default=True)
    time = models.TimeField(null=True)
    image = models.ImageField(null=True)
    easy_input = models.ForeignKey('EasyInput', null=True, on_delete=models.CASCADE, related_name='todo')

    def __str__(self):
        return "todo: " + self.title


class Keep(models.Model):
    goal = models.ForeignKey('Goal', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=True)
    time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return "keep: " + self.title


class EasyInput(models.Model):
    goal = models.ForeignKey('Goal', on_delete=models.CASCADE)
    title = models.CharField(max_length=20, blank=True)
    start_date = models.DateField(null=True, blank=True)
    finish_date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    days = models.ManyToManyField('Days')

    def __str__(self):
        return "easy: " + self.title


class Days(models.Model):
    day = models.CharField(max_length=5)


class TimeNotice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    time = models.TimeField()
