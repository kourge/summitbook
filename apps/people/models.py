from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.OneToOneField(User, unique=True)

    irc_nick = models.CharField(max_length=30, verbose_name="IRC nick")

    city = models.CharField(max_length=128)
    region = models.CharField(max_length=128)

    description = models.TextField(verbose_name="working on")
    other = models.TextField()

    # photo = models.ImageField()

class PhoneNumber(models.Model):
    person = models.ForeignKey(Person)
    number = models.CharField(max_length=64)

class IM(models.Model):
    person = models.ForeignKey(Person)
    im = models.CharField(max_length=64, verbose_name="IM")

