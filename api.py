"""
1. Read CSV file, then travel each row from a start index.
2. For each row, do this:
2.1. Determine Category base on the column contains transaction_note
2.2. Extract required data from the required row. Parse date and money
2.2.3 Combine 2.1 and 2.2 data into a dictionary
3. Persist dictionary to SQL lite
"""
