-- Sample SQL KPI Query
SELECT 
    Region,
    SUM(Revenue) AS Total_Revenue,
    SUM(Revenue - Cost) AS Total_Profit,
    AVG((Revenue - Cost) / Revenue) AS Avg_Margin
FROM sales_data
GROUP BY Region;
