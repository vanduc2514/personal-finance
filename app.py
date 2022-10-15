import csv
import string

import ingest

identifier = {
    'meal': ['foody', 'mc donalds', 'dining out', 'taco', 'savico'],
    'bike': ['moca'],
    'cafe': ['cafe'],
    'groceries': ['vinmart', 'sieu thi'],
    'cash_out': ['rut tien mat tai ATM']
}

output = {
    'meal': [],
    'bike': [],
    'cafe': [],
    'groceries': [],
    'cash_out': [],
}

transactions = ingest.vt_report_csv('202209050259.csv')

for transaction in transactions:
    transaction_note = transaction.note
    for keyword, category in identifier.items():
        for item in category:
            if item.lower() in transaction_note.lower():
                output.get(keyword).append(transaction)
                break


for k, v in output.items():
    print(k)
    for t in v:
        print(t)
