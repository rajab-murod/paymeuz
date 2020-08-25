from django.db import models


class Transaction(models.Model):
    STATUS = (
        (0, 'processing'),
        (1, 'success'),
        (2, 'failed'),
    )
    _id = models.CharField(max_length=255)
    amount = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    account = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, default=0, choices=STATUS)
    create_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.DateTimeField(auto_now=True)

