-- creates table states in database hbtn_0d_usa
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL UNIQUE AUTO_INCREMENT,
    name VARCHAR(256)
)