BEGIN
	CREATE TABLE IF NOT EXISTS  sw2.RANKING (
		r_id SERIAL PRIMARY KEY,
		r_usr varchar(100),
		r_puntos int,
		r_elim int NOT NULL,
		r_fecha date
	);
END
COMMIT
