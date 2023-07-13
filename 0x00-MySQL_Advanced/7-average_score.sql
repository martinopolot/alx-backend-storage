-- Write a SQL script that creates a stored procedure 
-- ComputeAverageScoreForUser. 
-- That computes and store the average score for a student. 
-- Note An average score can be a decimal
-- Procedure ComputeAverageScoreForUser is taking 1 input
-- user_id, a users.id value (you can assume user_id is linked to an existing users)
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
	UPDATE users
	SET average_score = (SELECT SUM(score) / COUNT(*) FROM corrections AS c WHERE c.user_id = user_id)
	WHERE id = user_id;
END;$$
DELIMITER ;
