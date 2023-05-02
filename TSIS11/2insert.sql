CREATE PROCEDURE p_insert(
	user_name VARCHAR,
	user_number VARCHAR
)
AS $$
INSERT INTO PHONEBOOK 
VALUES
(user_name, user_number);
$$;
CALL p_insert('Aika', '8 123 456 78 90')

CREATE PROCEDURE p_update(
    user_name VARCHAR,
    user_number VARCHAR
)
AS 
$$
UPDATE PHONEBOOK 
SET user_number= '8 123 456 70 90' 
WHERE user_name= 'Aika';
$$;
LANGUAGE plpgsql;

