CREATE PROCEDURE SPS_VER 
AS
BEGIN
	SELECT 
		r_usr,
		r_puntos,
		r_fecha
	FROM
		sw2.RANKING
	WHERE
		r_elim=0
	ORDER BY r_puntos DESC
	LIMIT 10
END
