from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    region = models.CharField(max_length=127)


class QuestionaryField(models.Model):
    title = models.CharField(max_length=255)
    parent_field = models.ForeignKey('self', null=True, blank=True, related_name='child_fields', on_delete=models.CASCADE)

    def __str__(self):
        return '({}) {}'.format(self.id, self.title)


class Questionary(models.Model):
    name = models.CharField(max_length=255)
    fields = models.ManyToManyField(QuestionaryField, related_name='questionaries', blank=True)

    def __str__(self):
        return '({}) {}'.format(self.id, self.name)


class FieldValue(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    questionary = models.ForeignKey(Questionary, on_delete=models.CASCADE)
    field = models.ForeignKey(QuestionaryField, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
