alter table products
ADD CONSTRAINT fk_categories_products
FOREIGN KEY (categoryid) REFERENCES categories(id)