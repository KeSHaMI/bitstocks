from decimal import Decimal

from django.db.transaction import atomic

from .models import Account, Transaction
from .exceptions import AccountBalanceTooLow


@atomic
def perform_deposit(user, amount):
    account = Account.objects.select_for_update().get(user=user)
    account.balance += Decimal(str(amount))
    account.save()

    transaction = Transaction.objects.create(
        account=account,
        transaction_type=Transaction.TRANSACTION_TYPE_DEPOSIT
    )

    return transaction


@atomic
def perform_withdrawal(user, amount):
    account = Account.objects.select_for_update().get(user=user)
    if amount < account.balance:
        account.balance -= Decimal(str(amount))
        account.save()
    else:
        raise AccountBalanceTooLow(f'Account balance is {account.balance} and amount is {amount}')

    transaction = Transaction.objects.create(
        account=account,
        transaction_type=Transaction.TRANSACTION_TYPE_DEPOSIT
    )

    return transaction
