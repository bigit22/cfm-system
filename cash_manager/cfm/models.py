from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone


class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'

    def __str__(self):
        return self.name


class TransactionType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Тип транзакции'
        verbose_name_plural = 'Типы транзакции'

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='subcategories')
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        return self.name


class Transaction(models.Model):
    created_at = models.DateTimeField(default=timezone.now)
    status = models.ForeignKey('Status', on_delete=models.SET_NULL, null=True)
    transaction_type = models.ForeignKey(
        'TransactionType', on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    comment = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'

    def __str__(self):
        return f"{self.created_at}: {self.transaction_type} - {self.amount:.2f} руб."

    def clean(self):
        if not self.category:
            raise ValidationError('Категория обязательна к заполнению.')
        if not self.subcategory:
            raise ValidationError('Подкатегория обязательна к заполнению.')
        if self.amount is None or self.amount <= 0:
            raise ValidationError(
                'Сумма обязательна к заполнению и должна быть положительной.')

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)
