import ingest

identifier = {
    'meal': ['foody', 'mc donalds', 'dining out', 'taco', 'savico', 'dinning out', 'meal'],
    'bike': ['moca'],
    'cafe': ['cafe', 'coffee'],
    'groceries': ['vinmart', 'sieu thi'],
    'cash_out': ['rut tien mat tai ATM'],
    'house': ['house'],
    'gift': ['gift']
}

# todo: make json and read identifier from it

# todo: init output map from input

output = dict((k, []) for (k, v) in identifier.items())

undetected = []

trans = ingest.vt_report_csv('202210232341.csv')

for transaction in trans:
    transaction_note = transaction.note.lower()
    for keyword, category in identifier.items():
        for item in category:
            if item.lower() in transaction_note:
                output.get(keyword).append(transaction)
                trans.remove(transaction)

for k, v in output.items():
    print(k)
    total = 0
    for t in v:
        print(t)
        total += t.amount
    print(total)

leftover = len(trans)
if leftover > 0:
    print('Undetected: ', leftover)
    for t in trans:
        print(t)
