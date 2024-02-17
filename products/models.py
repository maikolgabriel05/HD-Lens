from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Products(models.Model):
    name = models.CharField(verbose_name='Nome do Produto', max_length=100, null=False, blank=False)
    ncm = models.IntegerField(
        verbose_name='Ncm',
        validators=[MaxValueValidator(99999999)],
        null=True,
        blank=True
    )
    price = models.DecimalField(
        verbose_name='Preço',
        max_digits=10,  # Ajuste conforme necessário
        decimal_places=2,  # Ajuste conforme necessário
        null=True
    )
    stock = models.IntegerField(
        verbose_name='Quantidade em estoque',
        validators=[MaxValueValidator(9999999999), MinValueValidator(0)],
        null=True
    )
    manufacturing_date = models.DateField(auto_now=False)
    create_by = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        return self.name
