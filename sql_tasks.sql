-- First task

SELECT nb.title, count(*) as "count" FROM notebooks_notebook AS nn
    JOIN notebooks_brand AS nb ON nn.brand_id=nb.id GROUP BY nb.title ORDER BY count DESC;

-- Second task

SELECT width, depth, height, count(*) FROM (
SELECT  CASE
    WHEN mod(width::numeric, 10) BETWEEN 0.01 AND 5 THEN width + (5 - mod(width::numeric, 10))
    ELSE round(width::numeric, -1)
END AS "width",
    CASE
    WHEN mod(depth::numeric, 10) BETWEEN 0.01 AND 5 THEN depth + (5 - mod(depth::numeric, 10))
    ELSE round(depth::numeric, -1)
END AS "depth",
    CASE
    WHEN mod(height::numeric, 10) BETWEEN 0.01 AND 5 THEN height + (5 - mod(height::numeric, 10))
    ELSE round(height::numeric, -1)
END AS "height" FROM notebooks_notebook) AS result
GROUP BY width, depth, height ORDER BY width, depth, height;