from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField('Name', max_length=255)
    cnpj = models.CharField('CNPJ', max_length=14)

    def __str__(self) -> str:
        return f'{self.name}'