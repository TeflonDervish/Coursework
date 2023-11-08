-- ������������� (3 ��)
-- ������������� ������ + ������
CREATE OR ALTER VIEW PSandS AS
SELECT S.Price AS Pices, S.ServiceDescription, S.Limitations, S.RoomNumber, S.Equipment_ID, PS.* 
FROM Service S 
	JOIN PurchasedService PS ON S.Service_ID = PS.Service_ID

SELECT * FROM PSandS

-- ������ + �������
CREATE OR ALTER VIEW PSandV AS 
SELECT V.Surname, V.Name, V.PhoneNumber, V.Email, PS.* 
FROM Visitors V 
	JOIN PurchasedService PS ON V.Visitor_ID = PS.Visitor_ID

SELECT * 
FROM PSandV

-- ������ + ����������
CREATE OR ALTER VIEW PSandSt AS 
SELECT S.Surname, S.Name, S.MiddleName, S.PhoneNumber, S.LaborBookName, S.MedicalBookName, PS.* 
FROM Staff S 
	JOIN PurchasedService PS ON S.Staff_ID = PS.Staff_ID

SELECT * 
FROM PSandSt
--������������� ������������� + ������ �������� + ���������� (������ ���� ��������������)



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

--��������� (���������� ���-�� �����������, ������������)
--��������� (������� ���� � ���� ������������� ������ �� ������ ����)
--����������������� (���������� ������ ����� � ������� ��� ���������� �� ������������ �����)

--���������
CREATE OR ALTER FUNCTION dbo.GetStaffCount()
RETURNS INT
AS
BEGIN
	DECLARE @CountStaff INT
	SELECT @CountStaff = COUNT(Staff_ID)
	FROM Staff
	RETURN @CountStaff
END;

PRINT '���������� �����������: ' + CAST(dbo.GetStaffCount() AS VARCHAR(3))

--���������
CREATE OR ALTER FUNCTION dbo.GetPurchasedService(@RoomNum TINYINT)
RETURNS TABLE
AS
RETURN(
	SELECT PurchasedService.Price, PurchasedService.StartTime, PurchasedService.EndTime
	FROM Service
		JOIN PurchasedService ON Service.Service_ID=PurchasedService.Service_ID
	WHERE RoomNumber = @RoomNum)

SELECT *
FROM dbo.GetPurchasedService(3)

--�����������������
CREATE OR ALTER FUNCTION dbo.ServiceProfit(@StartDate SMALLDATETIME, @EndDate SMALLDATETIME)
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

SELECT * FROM ServiceProfit('2022-11-11 00:00:00', '2023-10-28 15:00:00')

-- !!!
-- ���������� �� ������ � ������������ �����
-- ������ - ���������
-- ����� - ���������


--������� �� ��������(���� �������� ������� ���������� � � ���� ���� ������ �� �� �������)
CREATE OR ALTER TRIGGER DeleteStaff
ON Staff
FOR DELETE
AS BEGIN
	DELETE Staff
	FROM deleted
	WHERE deleted.Staff_ID NOT IN (
		SELECT PurchasedService.Staff_ID 
		FROM PurchasedService
		WHERE PurchasedService.StartTime>=GETDATE())
END;

--������� �� ���������� � ���������(���� ������ ������ � ������� �������������� ������ ���� ���� ��������� �� ��������� ����������)
CREATE OR ALTER TRIGGER InsertService
ON PurchasedService
INSTEAD OF INSERT
AS BEGIN
	DECLARE @Start SMALLDATETIME
	DECLARE @End SMALLDATETIME
	DECLARE @Service TINYINT
	SELECT @Start = inserted.StartTime, @End = inserted.EndTime, @Service = inserted.Service_ID
	FROM inserted
	IF (SELECT COUNT(PurchasedService.PurchasedService_ID) 
		FROM PurchasedService
		WHERE (PurchasedService.StartTime BETWEEN @Start AND @End 
		OR PurchasedService.EndTime BETWEEN @Start AND @End) AND PurchasedService.Service_ID = @Service) <= 0
		INSERT INTO PurchasedService
		SELECT *
		FROM inserted
END;

CREATE OR ALTER TRIGGER UpdateService
ON PurchasedService
AFTER UPDATE
AS BEGIN
	DECLARE @Start SMALLDATETIME
	DECLARE @End SMALLDATETIME
	DECLARE @Service TINYINT
	SELECT @Start = inserted.StartTime, @End = inserted.EndTime, @Service = inserted.Service_ID
	FROM inserted
	IF (SELECT COUNT(PurchasedService.PurchasedService_ID) 
		FROM PurchasedService
		WHERE (PurchasedService.StartTime BETWEEN @Start AND @End 
		OR PurchasedService.EndTime BETWEEN @Start AND @End) AND PurchasedService.Service_ID = @Service) <= 0
		UPDATE PurchasedService
		SET 
			PurchasedService.Staff_ID=ins.Staff_ID, 
			PurchasedService.Visitor_ID=ins.Visitor_ID, 
			PurchasedService.Price=ins.Price, 
			PurchasedService.Service_ID=ins.Visitor_ID, 
			PurchasedService.StartTime=ins.StartTime, 
			PurchasedService.EndTime=ins.EndTime
		FROM PurchasedService
			JOIN inserted ins ON PurchasedService.PurchasedService_ID = ins.PurchasedService_ID;
END;
-- ������ (��� � �� ��� ��� �������� �� ������ ���� 3)
-- ������ �� �������� ���� �������� ���������� � ����������, � ������� ������������ ������ ID �������� �� NULL
-- ???
-- Staff_ID=ins.Staff_ID, Visitor_ID=ins.Visitor_ID, Price=ins.Price, Service_ID=ins.Visitor_ID, StartTime=ins.StartTime, EndTime=ins.EndTime