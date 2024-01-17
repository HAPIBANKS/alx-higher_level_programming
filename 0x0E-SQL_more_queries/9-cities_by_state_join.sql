-- lists all cities contained in the database hbn_od_usa
SELECT cities.id, cities.name, states.name
	FROM cities
	INNER JOIN states
	ON states.id = cities.state_id
	ORDER BY cities.id ASC;
