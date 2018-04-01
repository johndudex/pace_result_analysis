from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=250)
    subject_code = models.CharField(max_length=15)

    def __str__(self):
        return self.name