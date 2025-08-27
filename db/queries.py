CREATE_LIST = """
    CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product TEXT NOT NULL,
    bought INTEGER DEFAULT 0
    )
"""

INSERT_LIST = "INSERT INTO products (product) VALUES (?)"

SELECT_LIST = "SELECT id, product, bought FROM products"

SELECT_BOUGHT = "SELECT id, product, bought FROM products WHERE bought = 1"
SELECT_NOT_BOUGHT = "SELECT id, product, bought FROM products WHERE bought = 0"

UPDATE_LIST = "UPDATE products SET product = ? WHERE id = ?"

DELETE_LIST = "DELETE FROM products WHERE id = ?"