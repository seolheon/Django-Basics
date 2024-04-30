from django.db import models

class Animal(models.Model):
    name = models.CharField('Название', max_length=180)

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self) -> str:
        return self.name

class Note(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    content = models.TextField()

    class Meta:
        verbose_name = 'Записка'
        verbose_name_plural = 'Записки'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return self.name