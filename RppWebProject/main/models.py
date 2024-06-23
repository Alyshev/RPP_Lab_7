from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
class User(AbstractUser):
    user_role = models.CharField('user_role', max_length=200, default='user')


class City(models.Model):
    city = models.CharField('Город', max_length=20)

    def __str__(self):
        return f'{self.city}'


class Age(models.Model):
    age = models.IntegerField('Возраст')
    workExperience = models.IntegerField('Стаж работы')

    def __str__(self):
        return f'{self.workExperience}'


class WorkExperience(models.Model):
    city = models.OneToOneField(City, on_delete=models.CASCADE)
    workExperience = models.OneToOneField(Age, on_delete=models.CASCADE)
    positiom = models.CharField('Должность', max_length=20)

    def __str__(self):
        return f'{self.positiom}'


class FullName(models.Model):
    fullName = models.CharField('ФИО', max_length=20)

    def __str__(self):
        return f'{self.fullName}'


class Position(models.Model):
    id = models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')
    positiom = models.ForeignKey(WorkExperience, on_delete=models.CASCADE)
    fullName = models.ManyToManyField(FullName)
    payment = models.IntegerField("Выплата")

    def __str__(self):
        return f'№{self.id}'