from django.db import models

class Expense(models.Model):
    item = models.CharField(max_length=255)  # اسم المصروف
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # المبلغ

    def __str__(self):
        return f"{self.item} - {self.amount}"
