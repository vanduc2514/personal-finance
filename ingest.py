import csv
import string
from datetime import datetime

import util


def vt_report_csv(path: string, end=46, start=7) -> list[util.Transaction]:
    if path is None:
        pass
    transactions = []
    file = open(path, mode='r', encoding='UTF-8')
    report = csv.reader(file)
    for row in report:
        current = report.line_num
        # start point
        if start < current < end:
            # parsed date
            date = datetime.strptime(row[1], "%d/%m/%Y %H:%M:%S")
            amount = int(row[3].replace(',', '')) * -1
            transaction = util.Transaction(row[2], date, amount)
            transactions.append(transaction)
    return transactions
