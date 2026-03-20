WITH cte AS (
    SELECT 1 AS num
    UNION ALL
    SELECT num + 1
    FROM cte
    WHERE num < 1000
)
select top 1000 CAST(1000 + FLOOR(RAND(CHECKSUM(NEWID())) * 9000) AS INT) as pin from cte
order by newid()
OPTION (MAXRECURSION 10000)


