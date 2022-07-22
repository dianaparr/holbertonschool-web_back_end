-- Script that creates a view
-- Add task 11

DROP VIEW IF EXISTS `need_meeting`;
CREATE VIEW `need_meeting` AS SELECT `name` FROM `students`
WHERE `score` < 80 AND (`last_meeting` IS NULL OR `last_meeting` < ADDDATE(CURDATE(), INTERVAL -1 MONTH));
