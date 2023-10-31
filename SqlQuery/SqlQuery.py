import pyodbc


class SqlQuery():
    def __init__(self):
        self.connection_to_db = pyodbc.connect(
            'Driver={SQL Server};Server=TeflonDervish;Database=TrampolineCenter;Trusted_Connection=yes;')
        self.cursor = self.connection_to_db.cursor()

    def get_visitors(self):
        '''
        create table Visitors(
            Visitor_ID int primary key,
            Surname varchar(20),
            Name varchar(20),
            PhoneNumber varchar(15),
            Email varchar(25)
        )
        '''
        self.cursor.execute('SELECT * FROM Visitors')
        dict = {
            'Surname': [],
            'Name': [],
            'PhoneNumber': [],
            'Email': [],
        }
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            dict["Surname"].append(row[1])
            dict["Name"].append(row[2])
            dict["PhoneNumber"].append(row[3])
            dict["Email"].append(row[4])
        return dict

    def get_staff(self):
        '''
        create table Staff(
            Staff_ID int primary key,
            Surname varchar(20),
            Name varchar(20),
            MiddleName varchar(20),
            PhoneNumber varchar(15),
            LaborBookName int,
            MedicalBookName int,
        )
        '''
        self.cursor.execute('SELECT * FROM Staff')
        dict = {
            'Surname': [],
            'Name': [],
            'MiddleName': [],
            'PhoneNumber': [],
            'LaborBookName': [],
            'MedicalBookName': [],
        }
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            dict["Surname"].append(row[1])
            dict["Name"].append(row[2])
            dict["PhoneNumber"].append(row[3])
            dict["PhoneNumber"].append(row[4])
            dict["LaborBookName"].append(row[5])
            dict["MedicalBookName"].append(row[6])
        return dict

    def get_equipment(self):
        '''
        create table Equipment(
            Equipment_ID int primary key,
            Name varchar(20),
            Purpose varchar(300),
        )
        '''
        self.cursor.execute('SELECT * FROM Equipment')
        dict = {
            'Name': [],
            'Purpose': [],
        }
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            dict["Name"].append(row[1])
            dict["Purpose"].append(row[2])
        return dict

    def get_service(self):
        '''
        create table Service(
            Service_ID int primary key,
            Price decimal(8, 2),
            ServiceDescription varchar(300),
            Limitations varchar(300),
            RoomNumber tinyint,
            Equipment_ID int foreign key references Equipment(Equipment_ID),
        )
        '''
        self.cursor.execute('SELECT * FROM Service')
        dict = {
            'Price': [],
            'ServiceDescription': [],
            'Limitations': [],
            'RoomNumber': [],
            'Equipment_ID': [],
        }
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            dict["Price"].append(row[1])
            dict["ServiceDescription"].append(row[2])
            dict["Limitations"].append(row[3])
            dict["RoomNumber"].append(row[4])
            dict["Equipment_ID"].append(row[5])
        return dict

    def get_purchased_service(self):
        '''
        create table PurchasedService(
            PurchasedService_ID int primary key,
            Visitor_ID int foreign key references Visitors(Visitor_ID),
            Staff_ID int foreign key references Staff(Staff_ID),
            Service_ID int foreign key references Service(Service_ID),
            Price decimal(8, 2),
            StartTime smalldatetime,
            EndTime smalldatetime,
        )
        '''
        self.cursor.execute('SELECT * FROM PurchasedService')
        dict = {
            'Visitor_ID': [],
            'Staff_ID': [],
            'Service_ID': [],
            'Price': [],
            'StartTime': [],
            'EndTime': [],
        }
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            dict["Visitor_ID"].append(row[1])
            dict["Staff_ID"].append(row[2])
            dict["Service_ID"].append(row[3])
            dict["Price"].append(row[4])
            dict["StartTime"].append(row[5])
            dict["EndTime"].append(row[6])
        return dict

    # [Id, type, access]
    def chekc_password(self, login, password):
        self.cursor.execute('SELECT Visitor_ID, password FROM Visitor WHERE login = ' + login)
        ID = -1
        type = 'Visitor'
        access = -1
        passw = ''
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            ID = row[0]
            passw = row[1]

        if passw == password:
            return [ID, type, access]
        elif passw == '':
            type = 'Staff'
            self.cursor.execute('SELECT Visitor_ID, password, access_mod FROM Staff WHERE login = ' + login)
            while 1:
                row = self.cursor.fetchone()
                if not row: break
                ID = row[0]
                passw = row[1]
                access = row[2]
            if passw == password:
                return [ID, type, access]
        else:
            return [-1, 'Error', access]


