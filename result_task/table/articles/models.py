import datetime
from django.db import models
from django.utils import timezone


class Street(models.Model):
    name = models.TextField('street name')

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.TextField('human name')
    street = models.ForeignKey(Street, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def was_published_recently(self):
        return self.pub_date >= (timezone.now() - datetime.timedelta(days=7))
