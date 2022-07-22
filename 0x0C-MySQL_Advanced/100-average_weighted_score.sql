-- Script that creates a stored procedure
-- Advanced task

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser (`user_id` INT)
BEGIN
    DECLARE `avg_score_student` FLOAT;
    SET `avg_score_student` = (
        SELECT SUM(`score` * `weight`) / SUM(`weight`)
        FROM `users`
        JOIN `corrections` ON `users`.`id` = `corrections`.`user_id`
        JOIN `projects` ON `corrections`.`project_id` = `projects`.`id`
        WHERE `users`.`id` = `user_id`
    );
    UPDATE `users` SET `average_score` = `avg_score_student` WHERE `id` = `user_id`;
END;
//
