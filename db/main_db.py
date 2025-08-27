import sqlite3
from db import queries
from config import db_path


def init_db():
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.CREATE_LIST)
    conn.commit()
    conn.close()


def new_product(product):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.INSERT_LIST, (product,))
    conn.commit()
    product_id = cursor.lastrowid
    conn.close()
    return product_id


def shopping_list(filter_type='all'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if filter_type == 'bought':
        cursor.execute(queries.SELECT_BOUGHT)
    elif filter_type == 'not bought':
        cursor.execute(queries.SELECT_NOT_BOUGHT)
    else:
        cursor.execute(queries.SELECT_LIST)

    products = cursor.fetchall()
    conn.close()
    return products


def delete_product(product_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute(queries.DELETE_LIST, (product_id,))
    conn.commit()
    conn.close()


def update_product(product_id,new_product=None, bought=None):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if new_product is not None:
        cursor.execute(queries.UPDATE_LIST, (new_product, product_id))
    
    if bought is not None:
        cursor.execute("UPDATE products SET bought = ? WHERE id = ?", (bought, product_id))

    conn.commit()
    conn.close()
