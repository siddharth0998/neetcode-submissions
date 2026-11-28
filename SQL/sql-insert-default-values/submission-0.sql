CREATE TABLE products (
  id INTEGER PRIMARY KEY,
  name TEXT,
  stock INTEGER DEFAULT 0
);

-- Do not modify above this line --

insert into products (id,name,stock) values (1,'Apple',0),(2,'Banana',0),(3,'Orange',0);






-- Do not modify below this line --
SELECT * FROM products;
