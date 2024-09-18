from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    model = models.CharField(max_length=150, verbose_name='модель')
    create_data = models.DateField(verbose_name='дата выхода продукта на рынок')

    def __str__(self) -> str:
        return f'{self.name} {self.model}'

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"


class Link(models.Model):
    name = models.CharField(max_length=150, verbose_name='название')
    email = models.EmailField(max_length=150, verbose_name='почта', unique=True, null=True, blank=True)
    country = models.CharField(max_length=50, verbose_name='страна')
    city = models.CharField(max_length=50, verbose_name='город')
    street = models.CharField(max_length=50, verbose_name='улица', null=True, blank=True)
    house = models.CharField(max_length=50, verbose_name='номер дома', null=True, blank=True)
    products = models.ManyToManyField(Product, verbose_name='продукты', default=None)
    provider = models.ForeignKey('Link', on_delete=models.SET_NULL, verbose_name='поставщик', null=True, blank=True)
    debt = models.FloatField(default=0.00, verbose_name='задолженность перед поставщиком', null=True, blank=True)
    create_data = models.DateTimeField(verbose_name='время создания', auto_now_add=True, editable=False)

    def __str__(self) -> str:
        return f'{self.name}'

    class Meta:
        verbose_name = "звено"
        verbose_name_plural = "звенья"

