SELECT TOP 10 p.Name,
       SUM(sod.OrderQty) AS TotalQuantitySold
FROM Sales.SalesOrderDetail sod
JOIN Production.Product p 
     ON sod.ProductID = p.ProductID
GROUP BY p.Name
ORDER BY TotalQuantitySold DESC;

SELECT YEAR(soh.OrderDate) AS SalesYear,
       SUM(soh.TotalDue) AS TotalSales
FROM Sales.SalesOrderHeader soh
GROUP BY YEAR(soh.OrderDate)
ORDER BY SalesYear;

SELECT p.FirstName,
       p.LastName,
       e.JobTitle,
       d.Name AS DepartmentName
FROM HumanResources.Employee e
JOIN Person.Person p
     ON e.BusinessEntityID = p.BusinessEntityID
JOIN HumanResources.EmployeeDepartmentHistory dh
     ON e.BusinessEntityID = dh.BusinessEntityID
JOIN HumanResources.Department d
     ON dh.DepartmentID = d.DepartmentID
WHERE dh.EndDate IS NULL;

SELECT p.ProductID,
       p.Name
FROM Production.Product p
LEFT JOIN Sales.SalesOrderDetail sod
       ON p.ProductID = sod.ProductID
WHERE sod.ProductID IS NULL;

SELECT l.Name AS Location,
       p.Name AS Product,
       SUM(pi.Quantity) AS TotalQuantity
FROM Production.ProductInventory pi
JOIN Production.Product p
     ON pi.ProductID = p.ProductID
JOIN Production.Location l
     ON pi.LocationID = l.LocationID
GROUP BY l.Name, p.Name
ORDER BY l.Name, p.Name;