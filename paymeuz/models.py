from django.db import models


class Transaction(models.Model):
    PROCESS = 0
    PAID = 1
    FAILED = 2
    STATUS = (
        (PROCESS, 'processing'),
        (PAID, 'paid'),
        (FAILED, 'failed'),
    )

    trans_id = models.CharField(max_length=255)
    request_id = models.IntegerField()
    amount = models.DecimalField(decimal_places=2, default=0.00, max_digits=10)
    account = models.TextField(blank=True, null=True)
    state = models.IntegerField()
    status = models.CharField(max_length=10, default=PROCESS, choices=STATUS)
    create_time = models.DateTimeField(auto_now_add=True)
    pay_time = models.DateTimeField(auto_now=True)


    def create_transaction(self, trans_id, request_id, amount, account, state, status):
        self.objects.create(
            trans_id=trans_id,
            request_id=request_id,
            amount=amount / 100,
            account=account,
            state=state,
            status=status
        )

    def update_transaction(self, trans_id, state, status):
        trans = self.objects.get(trans_id=trans_id)
        trans.status = status
        trans.state = state
        trans.save()


