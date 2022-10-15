import numbers
import string
from datetime import datetime


class Transaction:
    """
    class to represent a Transaction
    """

    def __init__(self,
                 note: string,
                 date: datetime,
                 amount: numbers,
                 expense=True):
        self._note = note
        self._date = date
        self._amount: numbers = amount
        self._expense = expense

    @property
    def note(self):
        return self._note

    @note.getter
    def note(self):
        return self._note

    @property
    def date(self):
        return self._date

    @date.getter
    def date(self) -> datetime:
        return self._date

    @property
    def amount(self):
        return self._amount

    @amount.getter
    def amount(self):
        return self._amount

    @property
    def expense(self):
        return self._expense

    @expense.getter
    def expense(self):
        return self._expense

    def __str__(self) -> str:
        return str({
            'note': self.note,
            'date': str(self.date),
            'amount': self.amount,
            'expense': self.expense
        })
