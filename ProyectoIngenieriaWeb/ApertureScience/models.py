from django.db import models

# Create your models here.

class TestSubject(models.Model):
    number = models.IntegerField() #Especificar como clave primaria
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    birthdate = models.DateField()
    birthplace = models.CharField(max_length=100)

    def __str__(self):
        return str(self.number) + " - " + self.name + " " + self.surname

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.FloatField()
    version = models.CharField(max_length=10)

    def __str__(self):
        return self.name + " - " + self.version

class Experiment(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    successRate = models.FloatField()

    testSubjects = models.ManyToManyField(TestSubject,  related_name="experiments")
    #Cambiar la products por product porque solo hay un producto por experimento
    products = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="experiments")

    def __str__(self):
        return str(self.id) +" - "+ self.name