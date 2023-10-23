import pyodbc

connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=LAPTOP-E54KUOCI;Database=TrampolineCenter;Trusted_Connection=yes;')
cursor = connection_to_db.cursor()
cursor.execute('SELECT Surname FROM Visitors')
while 1:
    row = cursor.fetchone()
    if not row:
        break
    print(row.Surname)

connection_to_db.close()