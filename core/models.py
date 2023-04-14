from django.db import models

# Create your models here.

class Biodata(models.Model):
    first_name = models.CharField(max_length=200, null=True, blank=True)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self) :
        return self.emailpip