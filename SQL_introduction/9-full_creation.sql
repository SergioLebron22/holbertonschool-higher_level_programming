-- creates secon table in the database
CREATE TABLE second_table IF NOT EXISTS(
    id INT,
    name VARCHAR(256),
    score INT
);

-- Inserts data
INSERT INTO second_table (id, name, score)
VALUES
    (1, "John", 10),
    (2, "Alex", 3),
    (3, "Bob", 14),
    (4, "George", 8);
