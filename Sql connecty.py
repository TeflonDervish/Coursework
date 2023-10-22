import pyodbc

connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=WIN-6KLU4EI17UL;Database=test;Trusted_Connection=yes;')
cursor = connection_to_db.cursor()
cursor.execute('SELECT user_name, age FROM users')
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.user_name, row.age)

connection_to_db.close()q