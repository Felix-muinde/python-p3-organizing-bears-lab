-- Create the "bears" table
CREATE TABLE IF NOT EXISTS bears (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  age INT,
  sex CHAR(1),
  color VARCHAR(255),
  temperament VARCHAR(255),
  alive INT
);
