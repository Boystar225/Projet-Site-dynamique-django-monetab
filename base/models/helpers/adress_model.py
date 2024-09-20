from django.db import models

class AdressModel(models.Model):
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Adresse"
        verbose_name_plural = "Adresses"

    def __str__(self):
        return f"{self.street}, {self.city}"  