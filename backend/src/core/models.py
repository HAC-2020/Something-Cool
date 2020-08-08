from django.db import models

# Create your models here.


class BioOutput(models.Model):
    virus = models.CharField(max_length=100, null = True)
    protien = models.CharField(max_length=100, null = True)
    other = models.CharField(max_length=100, null = True)
    smile = models.CharField(max_length=100, null = True)
    description = models.CharField(max_length=100, null = True)
    timestamp = models.DateTimeField(auto_now_add=True, null = True)
    other_thing1 = models.CharField(max_length=100, null = True)
    other_thing2 = models.CharField(max_length=100, null = True)
    num1 = models.IntegerField(null=True)
    num2=models.IntegerField(null=True)

    def __str__(self):
        return self.protien