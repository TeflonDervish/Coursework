-- представления (3 шт)
--Приобретенные услуги + услуги
create or alter view PSandS as 
select S.*, PS.* from 
Service S join PurchasedService PS on S.Service_ID = PS.Service_ID

select * from PSandS
-- Услуги + клиенты
create or alter view PSandV as 
select V.*, PS.* from 
Visitors V join PurchasedService PS on V.Visitor_ID = PS.Visitor_ID

select * from PSandV
-- Услуги + сотрудники
create or alter view PSandSt as 
select S.*, PS.* from 
Staff S join PurchasedService PS on S.Staff_ID = PS.Staff_ID

select * from PSandSt



-- процедура 
-- добавление пакетов услуг(разные услуги) 
-- 1 пакет (батут на время 1 ,2, безлимит)
--Visitor ID, Stuff_ID, StartTime, Durability

DROP PROCEDURE FirstPack



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

-- функция(Скалярная возвращает кол-во сотрудников, мультифункци)
--Табличная
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

--Скалярная
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


-- статистику по услгам в определенное время
-- услуга - заработок
-- всего - заработок

-- тригер (Бля я не ебу что написать но короче надо 3)
-- ???