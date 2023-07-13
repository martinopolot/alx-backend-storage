-- Write a SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student
-- Procedure AddBonus is taking 3 inputs (in this order)
-- user_id, a users.id value, project_name, score
DELIMITER $$
CREATE PROCEDURE AddBonus(
    IN user_id int, IN project_name varchar(255), IN score float
)
BEGIN
    INSERT INTO projects (name) SELECT project_name FROM DUAL
    WHERE project_name NOT IN (SELECT name FROM projects);
    INSERT INTO corrections (user_id, project_id, score)
    VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;$$
DELIMITER ;
