use gym_2;
DELIMITER //

CREATE TRIGGER prevent_modification_on_programs
BEFORE UPDATE ON programs
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '45000'
    SET MESSAGE_TEXT = 'Modifications are not allowed on programs table.';
END //

DELIMITER ;

DELIMITER $$
CREATE TRIGGER validate_program_name
BEFORE INSERT ON programs
FOR EACH ROW
BEGIN
    IF NOT NEW.name REGEXP '^[AMZ]{1}[0-9]{5}[A-Za-z]{2}$' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Invalid program name format. Must be: 1 letter (A, M, or Z), 5 digits, and 2 random letters';
    END IF;
END $$

DELIMITER ;

DELIMITER //

CREATE TRIGGER prevent_double_zero_insert_on_programs
BEFORE INSERT ON programs
FOR EACH ROW
BEGIN
    IF RIGHT(NEW.name, 2) = '00' THEN
        SIGNAL SQLSTATE '45000'
        SET MESSAGE_TEXT = 'Values in name column cannot end with two zeros.';
    END IF;
END //

DELIMITER ;