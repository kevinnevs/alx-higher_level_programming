-- LISTS NUM OF RECORDS WITH SAME SCORE IN second_table
SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY score DESC;
