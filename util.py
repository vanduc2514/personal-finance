import string
from datetime import datetime


class Transaction:
    """
    class to represent a Transaction
    """

    def __init__(self,
                 note: string,
                 date: string,
                 amount: string,
                 expense=True):
        self.note = note
        self._date = date
        self.amount = amount
        self.expense = expense

    @property
    def date(self):
        return self._date

    @date.getter
    def date(self) -> datetime:
        return datetime.strptime(self._date, "%d/%m/%Y %H:%M:%S")

    def __str__(self) -> str:
        return str({
            'note': self.note,
            'date': str(self.date),
            'amount': self.amount,
            'expense': self.expense
        })
