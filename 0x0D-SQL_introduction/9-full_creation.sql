-- Display the number of records in the table 'first_table' where id = 89
SELECT COUNT(*) FROM first_table WHERE id = 89;

-- Create a new table 'second_table'
CREATE TABLE IF NOT EXISTS second_table (
    id INT,
    name VARCHAR(255),
    score INT
);

-- Insert some data into table 'second_table'
-- Names, John, Alex, Bob and George
-- Id 1,2,3,4  score, 10,3,14,8
INSERT INTO second_table (id, name, score) VALUES
(1, 'John', 10),
(2, 'Alex', 3),
(3, 'Bob', 14),
(4, 'George', 8)
;
