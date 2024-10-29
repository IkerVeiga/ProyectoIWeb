from django.db import models

# Create your models here.

class TestSubject(models.Model):
    number = models.IntegerField #Especificar como clave primaria
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField
    birthplace = models.CharField(max_length=100)

    def __str__(self):
        return self.number + " - " + self.name + " " + self.surname

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField

class Experiment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField

    testSubjects = models.ManyToManyField(TestSubject, related_name="experiments")
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="experiments")