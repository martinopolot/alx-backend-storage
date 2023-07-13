-- SQL script that creates a function SafeDiv
-- And returns a / b or 0 if b == 0
CREATE FUNCTION SafeDiv(a INT, b INT) RETURNS INT
BEGIN
    DECLARE result INT;

    IF b = 0 THEN
        SET result = 0;
    ELSE
        SET result = a / b;
    END IF;

    RETURN result;
END;
