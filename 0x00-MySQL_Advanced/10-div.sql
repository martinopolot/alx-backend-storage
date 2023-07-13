-- SQL script that creates a function SafeDiv
-- And returns a / b or 0 if b == 0
DELIMITER $$
CREATE FUNCTION SafeDiv (a INT, b INT) RETURNS FLOAT
BEGIN
    IF b = 0 THEN
    RETURN 0;
    ELSE
    RETURN a / b;
    END IF;
END;$$
DEMIMITER ;
