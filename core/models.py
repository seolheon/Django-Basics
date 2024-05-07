from django.db import models
from django.utils import timezone

class Animal(models.Model):
    name = models.CharField('Название', max_length=180)

    class Meta:
        verbose_name = 'Животное'
        verbose_name_plural = 'Животные'

    def __str__(self) -> str:
        return self.name

class Task(models.Model):

    PRIORITY_CHOICES = [('Low', 'Низкий'), ('Medium', 'Средний'), ('High', 'Высокий')]

    title = models.CharField('Название задачи', max_length=100)
    description = models.TextField(blank=True)
    due_date = models.DateField()
    priority = models.CharField('Приоритет', max_length=20, choices=PRIORITY_CHOICES)
    completed = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

    def __str__(self):
        return self.title

class Note(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField('Дата создания', default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Записка'
        verbose_name_plural = 'Записки'

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField('Дата создания', default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
    def __str__(self):
        return self.name
