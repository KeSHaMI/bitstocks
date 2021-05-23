from django.db import transaction
from .models import Account, Transaction


@transaction.atomic
def perform_deposit(user, amount):
    account = Account.objects.select_for_update().get(user=user)
    account.balance += amount
    account.save()

    transaction = Transaction.objects.create(
        account=account,
        transaction_type=Transaction.TRANSACTION_TYPE_DEPOSIT
    )

    return transaction

def perform_withdrawal(user, amount):
    pass
