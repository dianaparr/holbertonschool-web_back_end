-- Script that creates a trigger
-- Add task 5

DELIMITER //
CREATE TRIGGER `upd_email_check` BEFORE UPDATE ON `users`
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
    END IF;
END; //
