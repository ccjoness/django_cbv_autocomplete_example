from django.db import models


class ProgrammingLanguage(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Senator(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)
