create database TrampolineCenter;

drop table PurchasedService
drop table Service
drop table Visitors
drop table Staff
drop table Equipment

create table Visitors(
	Visitor_ID int primary key identity(0, 1),
	Surname varchar(20),
	Name varchar(20),
	PhoneNumber varchar(15),
	Email varchar(25),
	login varchar(20) not null,
	password varchar(20) not null 
)

create table Staff(
	Staff_ID int primary key identity(0, 1),
	Surname varchar(20),
	Name varchar(20),
	MiddleName varchar(20),
	PhoneNumber varchar(15),
	LaborBookName int,
	MedicalBookName int,
	login varchar(20) not null,
	password varchar(20) not null,
	access_mod tinyint,
)
create table Equipment(
	Equipment_ID int primary key identity(0, 1),
	Name varchar(20),
	Purpose varchar(300),
)

create table Service(
	Service_ID int primary key identity(0, 1),
	Price decimal(8, 2),
	ServiceDescription varchar(300),
	Limitations varchar(300),
	RoomNumber tinyint, 
	Equipment_ID int foreign key references Equipment(Equipment_ID) on delete set null,
)

create table PurchasedService(
	PurchasedService_ID int primary key identity(0, 1),
	Visitor_ID int foreign key references Visitors(Visitor_ID) on delete set null,
	Staff_ID int foreign key references Staff(Staff_ID) on delete set null,
	Service_ID int foreign key references Service(Service_ID) on delete set null,
	Price decimal(8, 2),
	StartTime smalldatetime, 
	EndTime smalldatetime,
)



INSERT INTO Visitors VALUES ('123', '123', '123', '123', '123', '123');