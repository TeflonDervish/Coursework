create database TrampolineCenter;

create table Visitors(
	Visitor_ID int primary key,
	Surname varchar(20),
	Name varchar(20),
	PhoneNumber varchar(15),
	Email varchar(25)

	# пароль
)

create table Staff(
	Staff_ID int primary key,
	Surname varchar(20),
	Name varchar(20),
	MiddleName varchar(20),
	PhoneNumber varchar(15),
	LaborBookName int,
	MedicalBookName int,

	# пароль
	# администратор или обычный сотрудник
)
create table Equipment(
	Equipment_ID int primary key,
	Name varchar(20),
	Purpose varchar(300),
)

create table Service(
	Service_ID int primary key,
	Price decimal(8, 2),
	ServiceDescription varchar(300),
	Limitations varchar(300),
	RoomNumber tinyint, 
	Equipment_ID int foreign key references Equipment(Equipment_ID),
)

create table PurchasedService(
	PurchasedService_ID int primary key,
	Visitor_ID int foreign key references Visitors(Visitor_ID),
	Staff_ID int foreign key references Staff(Staff_ID),
	Service_ID int foreign key references Service(Service_ID),
	Price decimal(8, 2),
	StartTime smalldatetime, 
	EndTime smalldatetime,

	#
)