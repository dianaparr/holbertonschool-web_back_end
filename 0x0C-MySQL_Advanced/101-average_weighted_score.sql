-- Script that creates a stored procedure
-- Advanced task two

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE `users`,
        (
            SELECT `users`.`id`, SUM(`score` * `weight`) / SUM(`weight`) AS `weight_avg`
            FROM `users`
            JOIN `corrections` ON `users`.`id` = `corrections`.`user_id`
            JOIN `projects` ON `corrections`.`project_id` = `projects`.`id`
            GROUP BY  `users`.`id`
        )
    AS `usr_av`
    SET `users`.`average_score` = `usr_av`.`weight_avg`
    WHERE `users`.`id` = `usr_av`.`id`;
END;
//
