from django.db import models


class Category(models.Model):
    title = models.CharField("Категории", max_length=100)

    def __str__(self):
        return self.title
    


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.CASCADE)
    title = models.CharField("Заголовок товара", max_length=255)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    image = models.ImageField("Фото", upload_to='uploads/', null=True, blank=True)
    
    def __str__(self):
        return self.title
    


