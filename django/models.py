from django.db import models

class Employee(models.Model):
    name = model.CharField(max_length=100)
    email = model.EmailField(unique=True)
    d_o_b = model.DateField()
    salary = model.FloatField()
    contact = model.PositiveIntegerField(unique=True)

    def __str__(self):
        return self.name