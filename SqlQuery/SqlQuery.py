import pyodbc


class SqlQuery():
    def __init__(self):
        self.connection_to_db = pyodbc.connect(
            'Driver={SQL Server};Server=LAPTOP-E54KUOCI;Database=TrampolineCenter;Trusted_Connection=yes;')
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
            'Visitor_ID': [],
            'Surname': [],
            'Name': [],
            'PhoneNumber': [],
            'Email': [],
            'login': [],
            'password': [],
        }
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            dict['Visitor_ID'].append(row[0])
            dict["Surname"].append(row[1])
            dict["Name"].append(row[2])
            dict["PhoneNumber"].append(row[3])
            dict["Email"].append(row[4])
            dict['login'].append(row[5])
            dict['password'].append(row[6])
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
            'Staff_ID': [],
            'Surname': [],
            'Name': [],
            'MiddleName': [],
            'PhoneNumber': [],
            'LaborBookName': [],
            'MedicalBookName': [],
            'login':[],
            'pasword':[],
            'access_mod':[],
        }
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            dict['Staff_ID'].append(row[0])
            dict["Surname"].append(row[1])
            dict["Name"].append(row[2])
            dict["MiddleName"].append(row[3])
            dict["PhoneNumber"].append(row[4])
            dict["LaborBookName"].append(row[5])
            dict["MedicalBookName"].append(row[6])
            dict["login"].append(row[7])
            dict["pasword"].append(row[8])
            dict["access_mod"].append(row[9])
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
            'Equipment_ID': [],
            'Name': [],
            'Purpose': [],
        }
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            dict['Equipment_ID'].append(row[0])
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
            'Service_ID': [],
            'Price': [],
            'ServiceDescription': [],
            'Limitations': [],
            'RoomNumber': [],
            'Equipment_ID': [],
        }
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            dict['Service_ID'].append(row[0])
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
        try:
            self.cursor.execute('SELECT * FROM PurchasedService')
            dict = {
                'PurchasedService_ID': [],
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
                dict["PurchasedService_ID"].append(row[0])
                dict["Visitor_ID"].append(row[1])
                dict["Staff_ID"].append(row[2])
                dict["Service_ID"].append(row[3])
                dict["Price"].append(row[4])
                dict["StartTime"].append(row[5])
                dict["EndTime"].append(row[6])
            return dict
        except:
            pass

    # [Id, type, access]
    def chekc_password(self, login, password):
        if login == '' or password == '':
            return [-1, 'Error']

        self.cursor.execute("SELECT Visitor_ID, password FROM Visitors WHERE login = '" + login + "'")
        ID = -1
        passw = ''
        while 1:
            row = self.cursor.fetchone()
            if not row: break
            ID = row[0]
            passw = row[1]
        print(passw)
        if passw == password:
            return [ID, "Visitor"]
        elif passw == '':
            access = -1
            self.cursor.execute("SELECT Staff_ID, password, access_mod FROM Staff WHERE login = '" + login + "'")
            while 1:
                row = self.cursor.fetchone()
                if not row: break
                ID = row[0]
                passw = row[1]
                access = row[2]
            if passw == password:
                if access == 1: return [ID, "Admin"]
                elif access == 0: return [ID, "Staff"]
            else:
                return [-1, 'Error']
        else:
            return [-1, 'Error']


    def sql_insert(self, table, values):

        text_query = 'INSERT INTO ' + table + ' VALUES ('
        print(values)
        for i in values:
            text_query += i + ', '

        text_query = text_query[:-2] + ");"
        print(text_query)
        try:
            self.cursor.execute(text_query)
            self.connection_to_db.commit()
        except:
            pass

    def query(self, text):
        print(text)
        try:
            self.cursor.execute(text)
        except:
            pass


    def get_staff_info(self, ID):
        try:
            self.cursor.execute('SELECT * FROM PSandV WHERE PSandV.Staff_ID = ' + str(ID))
            dict = {
                'Surname': [],
                'Name': [],
                'PhoneNumber': [],
                'Email': [],
                'Price': [],
                'StartTime': [],
                'EndTime': [],
            }
            while 1:
                row = self.cursor.fetchone()
                if not row: break
                dict["Surname"].append(row[0])
                dict["Name"].append(row[1])
                dict["PhoneNumber"].append(row[2])
                dict["Email"].append(row[3])
                dict["EndTime"].append(row[5])
                dict["Price"].append(row[6])
                dict["StartTime"].append(row[7])
                dict["EndTime"].append(row[8])
            return  dict
        except:
            pass

    def add_package(self, Package_ID, Visitor_ID, DateTime):
        try:
            print('EXEC ' + str(Package_ID) + ' ' + str(Visitor_ID) + ",NULL, '" + DateTime + "';")
            self.cursor.execute('EXEC ' + str(Package_ID) + ' ' + str(Visitor_ID) + ",NULL, '" + DateTime + "';")
            self.connection_to_db.commit()
        except:
            pass

    def sql_delete(self, table, Index_col, Id):
        try:
            print("DELETE FROM " + table + " WHERE " + Index_col + " = " + Id + ";")
            self.cursor.execute("DELETE FROM " + table + " WHERE " + Index_col + " = " + Id + ";")
        except:
            pass

    def sql_search(self, table, dict):
        text_query = "SELECT * FROM " + table + " WHERE "

        for i in dict:
            if i != '':
                text_query += i + " = " + dict[i] + ' and '
        print(text_query)

        self.cursor.execute(text_query)

    def user_info(self, Visitor_ID):
        try:
            self.cursor.execute('SELECT * FROM Visitors WHERE Visitor_ID = ' + str(Visitor_ID))
            user_data = self.cursor.fetchone()
            return user_data
        except:
            pass

    def service_profit(self, startTime, endTime):
        try:
            dict = {
                'Имя услуги': [],
                'Стоимость': []
            }
            self.cursor.execute(f"SELECT * FROM ServiceProfit('{startTime}', '{endTime}')")
            while 1:
                row = self.cursor.fetchone()
                if not row: break
                dict['Имя услуги'].append(row[0])
                dict['Стоимость'].append(row[1])
            return dict
        except:
            pass
