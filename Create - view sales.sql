CREATE VIEW Sales.vSalesByTerritory AS
SELECT t.Name AS Territory,
       SUM(soh.TotalDue) AS TotalSales
FROM Sales.SalesOrderHeader soh
JOIN Sales.SalesTerritory t
     ON soh.TerritoryID = t.TerritoryID
GROUP BY t.Name;