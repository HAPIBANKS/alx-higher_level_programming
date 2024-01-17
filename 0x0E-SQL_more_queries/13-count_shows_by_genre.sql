-- a script that lists all genres
USE hbtn_0d_tvshows;
SELECT
  genre AS genre,
  COUNT(*) AS number_of_shows
FROM
    shows
GROUP BY
    genre
HAVING
    COUNT(*) > 0
ORDER BY
    number_of_shows DESC;
