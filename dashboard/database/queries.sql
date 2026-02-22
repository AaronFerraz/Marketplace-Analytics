USE marketplace;
select * from Customers;







-- rank customers based on their total Orders Sales
/* WITH CustomerSales AS (
    SELECT 
        c.CustomerID,
        c.CustomerName,
        SUM(o.SalesAmount) AS TotalSales
    FROM 
        Customers c 
    INNER JOIN 
        Orders o ON c.CustomerID = o.CustomerID
    GROUP BY
        c.CustomerID, c.CustomerName
)
SELECT 
    CustomerID,
    CustomerName,
    TotalSales,
    RANK() OVER (ORDER BY TotalSales DESC) AS SalesRank
FROM 
    CustomerSales
ORDER BY
    -- TotalSales DESC;
*/