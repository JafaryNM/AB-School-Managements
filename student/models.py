from enum import unique
from re import T
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Exam(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Darasa(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100, null=True)
    surname = models.CharField(max_length=100)
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.first_name


class Results(models.Model):

    student= models.ForeignKey(Student, on_delete=models.CASCADE,null=True)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE,null=True)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE,null=True)
    darasa = models.ForeignKey(Darasa, on_delete=models.CASCADE,null=True)
    mark = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(100)] )
    
    def __str__(self):
        
        return f"{self.student} {self.exam} "


