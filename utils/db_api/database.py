import logging
import sqlite3

conn = sqlite3.connect('my.db')
cur = conn.cursor()

with conn:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Category (category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(128));
    """)

with conn:
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Product (product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    cpu VARCHAR(128),
    ram VARCHAR(128),
    display VARCHAR(128),
    color VARCHAR(128),
    price VARCHAR(128),
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES Category (category_id));
    """)


def write_category(category_name):
    try:
        with conn:
            cur.execute(" INSERT INTO Category (name) VALUES (?);", (category_name,))
            print('Category ga Saqlandi')
    except Exception:
        print('Category ga saqlashda xatolik')


def write_product(cpu, ram, display, color, price, category_id):
    try:
        with conn:
            cur.execute(
                " INSERT INTO Product (cpu, ram, display, color, price, category_id) VALUES (?, ?, ?, ?, ?, ?);",
                (cpu, ram, display, color, price, category_id))
            print('Product ga Saqlandi')
    except Exception:
        print('Product ga saqlashda xatolik')