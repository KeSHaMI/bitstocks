from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Account(models.Model):
    """
    Client account to hold currency
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    balance = models.DecimalField('balance', default=0, decimal_places=10, max_length=12, max_digits=12)


class Transaction(models.Model):
    """
    Transaction explaining the change of an account balance: deposits, withdrawal, etc.
    """
    TRANSACTION_TYPE_DEPOSIT = 1
    TRANSACTION_TYPE_WITHDRAWAL = 2

    transaction_type = models.PositiveIntegerField(
        'transaction type',
        choices=(
            (TRANSACTION_TYPE_DEPOSIT, 'deposit'),
            (TRANSACTION_TYPE_WITHDRAWAL, 'withdrawal'),
        )
    )

    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    datetime = models.DateTimeField('time', default=timezone.now)

