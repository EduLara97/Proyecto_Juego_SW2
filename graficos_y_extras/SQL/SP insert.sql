CREATE PROCEDURE SPI_REG  (@r_usr INT, @r_puntos INT) 
AS
BEGIN
	INSERT INTO sw2.RANKING
	VALUES (@r_usr, @r_puntos,0,NOW())
END