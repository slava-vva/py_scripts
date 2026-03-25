SELECT 
    p.FirstName, 
    p.LastName, 
    e.JobTitle
FROM HumanResources.Employee AS e
JOIN Person.Person AS p 
    ON e.BusinessEntityID = p.BusinessEntityID
ORDER BY e.JobTitle ASC;

--Joins and Filtering
SELECT 
    Name, 
    ProductNumber, 
    SellStartDate, 
    ProductLine
FROM Production.Product
WHERE SellStartDate IS NOT NULL 
    AND ProductLine = 'T';
