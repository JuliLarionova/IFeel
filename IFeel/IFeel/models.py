from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    region = models.CharField(max_length=127)

    def to_json(self):
        return {
            'username': self.username,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'id': self.id,
        }


class QuestionaryField(models.Model):
    title = models.CharField(max_length=255)
    parent_field = models.ForeignKey('self', null=True, blank=True, related_name='child_fields',
                                     on_delete=models.CASCADE)
    speech_code = models.CharField(max_length=255, default="")

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'parent': (None if self.parent_field is None else self.parent_field.to_json()),
            'speech_code': self.speech_code
        }

    def __str__(self):
        return '({}) {}'.format(self.id, self.title)


class Template(models.Model):
    name = models.CharField(max_length=255)
    fields = models.ManyToManyField(QuestionaryField, related_name='questionaries', blank=True)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'fields': [
                x.to_json() for x in self.fields.all()
            ]
        }

    def __str__(self):
        return '({}) {}'.format(self.id, self.name)


class Questionary(models.Model):
    template = models.ForeignKey(Template, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def to_json(self):
        field_id_to_value = dict()
        for x in self.fieldvalue_set.all():
            field_id_to_value[x.field_id] = x.value
        return {
            'id': self.id,
            'author': self.author.to_json(),
            'template': self.template.to_json(),
            'fields': [
                {
                    'field': x.to_json(),
                    'value': field_id_to_value.get(x.id),
                } for x in self.template.fields.all()
            ]
        }


class FieldValue(models.Model):
    ctime = models.DateTimeField(auto_now_add=True)
    mtime = models.DateTimeField(auto_now=True)
    questionary = models.ForeignKey(Questionary, on_delete=models.CASCADE)
    field = models.ForeignKey(QuestionaryField, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
