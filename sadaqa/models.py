from django.db import models

class Donation(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    recipient = models.CharField(max_length=255)
    date = models.DateField()
    type = models.CharField(max_length=100)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f"{self.recipient} - {self.amount}"
