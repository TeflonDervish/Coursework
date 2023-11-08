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


CREATE OR ALTER PROCEDURE FirstPack
    @VisitorID int, @StuffID int AS
BEGIN
	SELECT P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime ,P.EndTime FROM PurchasedService P
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 7, GETDATE(), GETDATE())

END;
EXEC FirstPack 1,1;

-- 2 пакет (аниматов + батутов + комнатв)
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

-- 3 пакет (аниматов + гигагейпузыри + батутов + комнатв)
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


-- 4 пакет (аниматов + пиньят + батутв + комнатв)
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

-- 5 пакет (аниматов + гигпуз + пиньят + батутв + комнатв)
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


-- 6 бичпакет (батут+ комната)
CREATE OR ALTER PROCEDURE FirstPack
    @VisitorID int, @StuffID int AS
BEGIN
	SELECT P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime ,P.EndTime FROM PurchasedService P
	insert into PurchasedService (P.Visitor_ID, P.Staff_ID, P.Service_ID, P.StartTime, P.EndTime) values
	(@VisitorID, @StuffID, 5, GETDATE(), GETDATE()),
	(@VisitorID, @StuffID, 1, GETDATE(), GETDATE())

END;
EXEC FirstPack 1,1;

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
-- тригер (Бля я не ебу что написать но короче надо 3)
-- тригер на удаление если удаление посетителя и сотрудника, в таблице приобретнные услуги ID меняется на NULL
-- ???
-- Staff_ID=ins.Staff_ID, Visitor_ID=ins.Visitor_ID, Price=ins.Price, Service_ID=ins.Visitor_ID, StartTime=ins.StartTime, EndTime=ins.EndTime