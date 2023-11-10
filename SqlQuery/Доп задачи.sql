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
    @VisitorID int, @StuffID int, @StartTime smalldatetime AS
BEGIN
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 6, 350, @StartTime, DATEADD(HOUR,1,@StartTime))

END;
EXEC Pack1 2,1,'2020-11-1 12:00';

-- 2 пакет (аниматов + батутов + комнатв)
CREATE OR ALTER PROCEDURE Pack2
    @VisitorID int, @StuffID int,@StartTime smalldatetime AS
BEGIN
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 4,2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 6, 350 , DATEADD(HOUR,1,@StartTime), DATEADD(HOUR,2,@StartTime)),
	(@VisitorID, @StuffID, 1, 2000, DATEADD(HOUR,2,@StartTime), DATEADD(HOUR,3,@StartTime))

END;
EXEC Pack2 2,1,'2020-11-1 12:00';

-- 3 пакет (аниматов + гигапузыри + батутов + комнатв)
CREATE OR ALTER PROCEDURE Pack3
    @VisitorID int, @StuffID int,@StartTime smalldatetime AS
BEGIN
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 4, 2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 7, 999.99, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 6, 350, DATEADD(HOUR,1,@StartTime), DATEADD(HOUR,2,@StartTime)),
	(@VisitorID, @StuffID, 1, 2000, DATEADD(HOUR,2,@StartTime), DATEADD(HOUR,3,@StartTime))

END;
EXEC Pack3 2,1,'2020-11-1 10:00';


-- 4 пакет (аниматов + пиньят + батутв + комнатв)
CREATE OR ALTER PROCEDURE Pack4
    @VisitorID int, @StuffID int,@StartTime smalldatetime AS
BEGIN
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 4, 2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 8, 2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 6, 350, DATEADD(HOUR,1,@StartTime), DATEADD(HOUR,2,@StartTime)),
	(@VisitorID, @StuffID, 3, 2000, DATEADD(HOUR,2,@StartTime), DATEADD(HOUR,3,@StartTime))

END;
EXEC Pack4 2,1,'2020-11-1 10:00';

-- 5 пакет (аниматов + гигпуз + пиньят + батутв + комнатв)
CREATE OR ALTER PROCEDURE Pack5
    @VisitorID int, @StuffID int,@StartTime smalldatetime AS
BEGIN
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 4, 2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 7, 999.99, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 8, 2200, @StartTime, DATEADD(HOUR,1,@StartTime)),
	(@VisitorID, @StuffID, 6, 350, DATEADD(HOUR,1,@StartTime), DATEADD(HOUR,2,@StartTime)),
	(@VisitorID, @StuffID, 2, 2000, DATEADD(HOUR,2,@StartTime), DATEADD(HOUR,3,@StartTime))

END;
EXEC Pack5 2,1,'2020-11-01 10:00';

-- 6 пакет (батут+ комната)
CREATE OR ALTER PROCEDURE Pack6
    @VisitorID int, @StuffID int,@StartTime smalldatetime AS
BEGIN
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.Price, P.StartTime, P.EndTime) values
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

--Мультиоператорная
CREATE OR ALTER FUNCTION dbo.ServiceProfit(@StartDate DATETIME, @EndDate DATETIME)
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

--Триггер на добавление и изменение(если меняем запись в таблице приобретенноый услуги если даты совпадают не разрешаем добавление)
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
	SELECT Surname, Name, MiddleName, PhoneNumber,LaborBookName, MedicalBookName, login, password, access_mod
	FROM inserted
END;
CREATE OR ALTER TRIGGER UniqueLoginVisitors
ON Visitors
AFTER INSERT, UPDATE
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

-- тригер на удаление если удаление посетителя и сотрудника, в таблице приобретнные услуги ID меняется на NULL
-- ???
-- Staff_ID=ins.Staff_ID, Visitor_ID=ins.Visitor_ID, Price=ins.Price, Service_ID=ins.Visitor_ID, StartTime=ins.StartTime, EndTime=ins.EndTime
