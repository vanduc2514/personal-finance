import string


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
        self.date = date
        self.amount = amount
        self.expense = expense

    def __str__(self) -> str:
        return str({
            'note': self.note,
            'date': self.date,
            'amount': self.amount,
            'expense': self.expense
        })
