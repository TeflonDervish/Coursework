-- ������������� (3 ��)
--������������� ������ + ������
create or alter view PSandS as 
select S.*, PS.* from 
Service S join PurchasedService PS on S.Service_ID = PS.Service_ID

select * from PSandS
-- ������ + �������
create or alter view PSandV as 
select V.*, PS.* from 
Visitors V join PurchasedService PS on V.Visitor_ID = PS.Visitor_ID

select * from PSandV
-- ������ + ����������
create or alter view PSandSt as 
select S.*, PS.* from 
Staff S join PurchasedService PS on S.Staff_ID = PS.Staff_ID

select * from PSandSt
-- !!! ������������� ������������� + ������ �������� + ���������� (������ ���� ��������������)


-- ��������� 
-- ���������� ������� �����(������ ������) 
-- 1 ����� (����� �� ����� 1 ,2, ��������)
--Visitor ID, Stuff_ID, StartTime, Durability


CREATE OR ALTER PROCEDURE FirstPack
    @VisitorID int, @StuffID int AS
BEGIN
	SELECT P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime ,P.EndTime FROM PurchasedService P
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 7, GETDATE(), GETDATE())

END;
EXEC FirstPack 1,1;

-- 2 ����� (�������� + ������� + �������)
CREATE OR ALTER PROCEDURE FirstPack
    @VisitorID int, @StuffID int AS
BEGIN
	SELECT P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime ,P.EndTime FROM PurchasedService P
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 7, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 5, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 1, GETDATE(), GETDATE())

END;
EXEC FirstPack 1,1;

-- 3 ����� (�������� + ������������� + ������� + �������)
CREATE OR ALTER PROCEDURE FirstPack
    @VisitorID int, @StuffID int AS
BEGIN
	SELECT P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime ,P.EndTime FROM PurchasedService P
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 7, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 8, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 5, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 1, GETDATE(), GETDATE())

END;
EXEC FirstPack 1,1;


-- 4 ����� (�������� + ������ + ������ + �������)
CREATE OR ALTER PROCEDURE FirstPack
    @VisitorID int, @StuffID int AS
BEGIN
	SELECT P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime ,P.EndTime FROM PurchasedService P
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 7, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 9, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 5, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 1, GETDATE(), GETDATE())

END;
EXEC FirstPack 1,1;

-- 5 ����� (�������� + ������ + ������ + ������ + �������)
CREATE OR ALTER PROCEDURE FirstPack
    @VisitorID int, @StuffID int AS
BEGIN
	SELECT P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime ,P.EndTime FROM PurchasedService P
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 7, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 8, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 9, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 5, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 1, GETDATE(), GETDATE())

END;
EXEC FirstPack 1,1;


-- 6 �������� (�����+ �������)
CREATE OR ALTER PROCEDURE FirstPack
    @VisitorID int, @StuffID int AS
BEGIN
	SELECT P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime ,P.EndTime FROM PurchasedService P
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 5, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 1, GETDATE(), GETDATE())

END;
EXEC FirstPack 1,1;

-- �������(��������� ���������� ���-�� �����������, ������������)
--!!!���������(��� - ������)
--!!!�����������������(���������� ������ ����� � ������� ��� ���������� �� ������������ �����)

create or ALTER FUNCTION dbo.ServiceProfit(@StartDate SMALLDATETIME, @EndDate SMALLDATETIME)
RETURNS @Profit Table(
	NameProfit VARCHAR(20),
	PriceProfit DECIMAL(8,2))
AS BEGIN
	INSERT @Profit
	SELECT Equipment.Name, SUM(PurchasedService.Price) 
	FROM PurchasedService
		JOIN Service ON PurchasedService.Service_ID=Service.Service_ID
		JOIN Equipment ON Service.Equipment_ID=Equipment.Equipment_ID
	WHERE PurchasedService.StartTime BETWEEN @StartDate AND @EndDate
	GROUP BY Equipment.Name
	RETURN
END;

select * from ServiceProfit('2022-11-11 00:00:00', '2023-10-28 15:00:00')

--���������
CREATE OR ALTER FUNCTION GetStaffCount()
RETURNS INT
AS
BEGIN
  
    RETURN (
        SELECT COUNT(*)
        FROM Staff
    );
END;

PRINT dbo.GetStaffCount()

-- !!!
-- ���������� �� ������ � ������������ �����
-- ������ - ���������
-- ����� - ���������

-- ������ (��� � �� ��� ��� �������� �� ������ ���� 3)
-- ������ �� �������� ���� �������� ���������� � ����������, � ������� ������������ ������ ID �������� �� NULL
-- ???