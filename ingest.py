import csv
import string

import util


def vt_report_csv(path: string, end=36, start=7) -> list[util.Transaction]:
    if path is None:
        pass
    transactions = []
    file = open(path, mode='r', encoding='UTF-8')
    report = csv.reader(file)
    for row in report:
        current = report.line_num
        # start point
        if start < current < end:
            transaction = util.Transaction(row[2], row[1], row[3])
            transactions.append(transaction)
    return transactions
