-- представления (3 шт)
-- Приобретенные услуги + услуги
CREATE OR ALTER VIEW PSandS AS
SELECT S.Price AS Pices, S.ServiceDescription, S.Limitations, S.RoomNumber, S.Equipment_ID, PS.* 
FROM Service S 
	JOIN PurchasedService PS ON S.Service_ID = PS.Service_ID

SELECT * FROM PSandS

-- Услуги + клиенты
CREATE OR ALTER VIEW PSandV AS 
SELECT V.Surname, V.Name, V.PhoneNumber, V.Email, PS.* 
FROM Visitors V 
	JOIN PurchasedService PS ON V.Visitor_ID = PS.Visitor_ID

SELECT * 
FROM PSandV

-- Услуги + сотрудники
CREATE OR ALTER VIEW PSandSt AS 
SELECT S.Surname, S.Name, S.MiddleName, S.PhoneNumber, S.LaborBookName, S.MedicalBookName, PS.* 
FROM Staff S 
	JOIN PurchasedService PS ON S.Staff_ID = PS.Staff_ID

SELECT * 
FROM PSandSt
--представление приобретенные + услуги персонал + посетители (должен быть модифицируемым)



-- процедура 
-- добавление пакетов услуг(разные услуги) 
-- 1 пакет (батут на время 1 ,2, безлимит)
--Visitor ID, Stuff_ID, StartTime, Durability


CREATE OR ALTER PROCEDURE Pack1
    @VisitorID int, @StuffID int, @StartTime SMALLDATETIME AS
BEGIN
	INSERT INTO PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) VALUES
	(@VisitorID, @StuffID, 6, 350, @StartTime, DATEADD(HOUR,1,@StartTime))

END;
EXEC Pack1 2,1,'2020-11-1 12:00';

-- 2 пакет (аниматов + батутов + комнатв)
CREATE OR ALTER PROCEDURE Pack2
    @VisitorID int, @StuffID int,@StartTime SMALLDATETIME AS
BEGIN
	INSERT INTO PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) VALUES
	(@VisitorID, @StuffID, 4,2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 6, 350 , DATEADD(HOUR,1,@StartTime), DATEADD(HOUR,2,@StartTime)),
	(@VisitorID, @StuffID, 1, 2000, DATEADD(HOUR,2,@StartTime), DATEADD(HOUR,3,@StartTime))
END;
EXEC Pack2 2,1,'2020-11-1 12:00';

-- 3 пакет (аниматов + гигапузыри + батутов + комнатв)
CREATE OR ALTER PROCEDURE Pack3
    @VisitorID INT, @StuffID INT,@StartTime SMALLDATETIME AS
BEGIN
	INSERT INTO PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) VALUES
	(@VisitorID, @StuffID, 4, 2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 7, 999.99, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 6, 350, DATEADD(HOUR,1,@StartTime), DATEADD(HOUR,2,@StartTime)),
	(@VisitorID, @StuffID, 1, 2000, DATEADD(HOUR,2,@StartTime), DATEADD(HOUR,3,@StartTime))
END;
EXEC Pack3 2,1,'2020-11-1 10:00';


-- 4 пакет (аниматов + пиньят + батутв + комнатв)
CREATE OR ALTER PROCEDURE Pack4
    @VisitorID INT, @StuffID INT,@StartTime SMALLDATETIME AS
BEGIN
	INSERT INTO PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) VALUES
	(@VisitorID, @StuffID, 4, 2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 8, 2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 6, 350, DATEADD(HOUR,1,@StartTime), DATEADD(HOUR,2,@StartTime)),
	(@VisitorID, @StuffID, 3, 2000, DATEADD(HOUR,2,@StartTime), DATEADD(HOUR,3,@StartTime))
END;
EXEC Pack4 2,1,'2020-11-1 10:00';

-- 5 пакет (аниматов + гигпуз + пиньят + батутв + комнатв)
CREATE OR ALTER PROCEDURE Pack5
    @VisitorID INT, @StuffID INT,@StartTime SMALLDATETIME AS
BEGIN
	INSERT INTO PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) VALUES
	(@VisitorID, @StuffID, 4, 2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 7, 999.99, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 8, 2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 6, 350, DATEADD(HOUR,1,@StartTime), DATEADD(HOUR,2,@StartTime)),
	(@VisitorID, @StuffID, 2, 2000, DATEADD(HOUR,2,@StartTime), DATEADD(HOUR,3,@StartTime))
END;
EXEC Pack5 2,1,'2020-11-1 10:00';


-- 6 пакет (батут+ комната)
CREATE OR ALTER PROCEDURE Pack6
    @VisitorID INT, @StuffID INT,@StartTime SMALLDATETIME AS
BEGIN
	INSERT INTO PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) VALUES
	(@VisitorID, @StuffID, 6, 350, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 0, 2000, DATEADD(HOUR,1,@StartTime), DATEADD(HOUR,2,@StartTime))
END;
EXEC Pack6 2,1,'2020-11-1 10:00';

--Скалярная (возвращает кол-во сотрудников, мультифункци)
--Табличная (выводит цену и дату приобретенной услуги по номеру зала)
--Мультиоператорная (возварщает список услуг и сколько они заработали за определенное время)

--Скалярная
CREATE OR ALTER FUNCTION dbo.GetStaffCount()
RETURNS INT
AS
BEGIN
	DECLARE @CountStaff INT
	SELECT @CountStaff = COUNT(Staff_ID)
	FROM Staff
	RETURN @CountStaff
END;

PRINT 'Количество сотрудников: ' + CAST(dbo.GetStaffCount() AS VARCHAR(3))

--Табличная
CREATE OR ALTER FUNCTION dbo.GetPurchasedService(@RoomNum TINYINT, @StartDate SMALLDATETIME, @EndDate SMALLDATEtIME)
RETURNS TABLE
AS
RETURN(
	SELECT Equipment.Name, PurchasedService.StartTime, PurchasedService.EndTime
	FROM Equipment
		JOIN Service ON Service.Equipment_ID=Equipment.Equipment_ID
		JOIN PurchasedService ON Service.Service_ID=PurchasedService.Service_ID
	WHERE RoomNumber = @RoomNum AND (@StartDate <= PurchasedService.StartTime AND @EndDate >= PurchasedService.EndTime))

SELECT *
FROM dbo.GetPurchasedService(14, '2000-01-01', '2023-30-06')

--Мультиоператорная
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

SELECT * FROM ServiceProfit('2019-28-11 00:00', '2024-10-12 15:00')

-- !!!
-- статистику по услгам в определенное время
-- услуга - заработок
-- всего - заработок


--Триггер на удаление(если пытаемся удалить сотрудника и у него есть работа то не удаляем)
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

DELETE Staff
WHERE Staff_ID=5

--Триггер на добавление и изменение(нельзя одинаковые логины)
CREATE OR ALTER TRIGGER UniqueLogin
ON Staff
INSTEAD OF INSERT, UPDATE
AS BEGIN
	DECLARE @Login VARCHAR(20)
	SELECT @Login = inserted.login
	FROM inserted
	IF (SELECT COUNT(login) 
		FROM Staff
		WHERE Staff.login = @Login) <= 0
	INSERT INTO Staff
	SELECT Surname, Name, MiddleName, PhoneNumber, LaborBookName, MedicalBookName, login, password, access_mod
	FROM inserted
END;

INSERT INTO Staff
VALUES ('sfvrvv', 'midvss', 'sveev', 1452, 1233, 36522, '123', '325', NULL)

UPDATE Staff
SET Login = '123'
WHERE Staff_ID=48

--Триггер на добавление и изменение(нельзя одинаковые логины)
CREATE OR ALTER TRIGGER UniqueLoginVisitors
ON Visitors
INSTEAD OF INSERT, UPDATE
AS BEGIN
	DECLARE @Login VARCHAR(20)
	SELECT @Login = inserted.Login
	FROM inserted
	IF (SELECT COUNT(Login) 
		FROM Visitors
		WHERE Visitors.Login = @Login) > 0
	BEGIN
		ROLLBACK
	END
	ELSE
		INSERT INTO Visitors
		SELECT Surname, Name, PhoneNumber, Email, login, password
		FROM inserted
END;

INSERT INTO Visitors
VALUES ('sfvrvv', 'midvss', 1452, 'dsvrev', 'efhhef', '325')

UPDATE Visitors
SET Login = '123'
WHERE Visitor_ID=5

--Триггер на одно и тоже время нельзя одну комнату
CREATE OR ALTER TRIGGER dbo.UniqueRoom
ON PurchasedService
AFTER INSERT, UPDATE
AS BEGIN
	DECLARE @Start SMALLDATETIME
	DECLARE @End SMALLDATETIME
	DECLARE @RoomNumber TINYINT
	SELECT @Start = inserted.StartTime, @End = inserted.EndTime, @RoomNumber = RoomNumber
	FROM inserted
		JOIN Service ON inserted.Service_ID=Service.Service_ID
	IF (SELECT COUNT(PurchasedService.PurchasedService_ID) 
		FROM PurchasedService
			JOIN Service ON PurchasedService.Service_ID=Service.Service_ID
		WHERE (PurchasedService.StartTime BETWEEN @Start AND @End 
		OR PurchasedService.EndTime BETWEEN @Start AND @End) AND Service.RoomNumber = @RoomNumber) <= 0
		INSERT INTO PurchasedService
		SELECT Visitor_ID, Staff_ID, Service_ID, Price, StartTime, EndTime
		FROM inserted
END;


UPDATE Visitors SET Surname = '1', Name = '1', PhoneNumber = '1', Email = '1', login = '1', password = '1' WHERE Visitor_ID = 66;