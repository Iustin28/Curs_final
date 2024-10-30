import pandas
import mysql.connector
from password import parola
import csv
import random
from datetime import datetime, timedelta

# df = pandas.read_csv('orders.csv', header=None)
# data_list=[]
my_db = mysql.connector.connect(host='localhost',
                                user='root',
                                password=parola,
                                database='proiect_final'
                                )

cursor = my_db.cursor()
# cursor.execute("CREATE DATABASE proiect_final")

# cursor.execute('CREATE TABLE orders (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'order_id INT,'
#                'customer_id INT,'
#                'product_id INT,'
#                'sale_date DATE,'
#                'quantity INT,'
#                'price DECIMAL(10,2))')
#
# cursor.execute('SHOW TABLES')
# for x in cursor:
#     print(x)
#
# cursor.execute('CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'customer_id INT,'
#                'name VARCHAR(250),'
#                'email VARCHAR(250),'
#                'country VARCHAR(150),'
#                'registration_date Date)')


# cursor.execute('CREATE TABLE products (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'product_id INT,'
#                'product_name VARCHAR(250),'
#                'category VARCHAR(50),'
#                'stock VARCHAR(50))')
#

# cursor.execute('CREATE TABLE reviews (id INT AUTO_INCREMENT PRIMARY KEY,'
#                'review_id INT,'
#                'customer_id INT,'
#                'product_id INT,'
#                'rating INT CHECK (rating BETWEEN 1 AND 5),'
#                'review_date Date)')

#df read.csv - functie

#df = pandas.read_sql(query, my_db)


#cursor = db_connection.cursor()

# 1. Cei mai activi clienți (top 10 clienți după numărul de comenzi)
cursor.execute("""
    SELECT customer_id, COUNT(order_id) AS order_id
    FROM orders
    GROUP BY customer_id
    ORDER BY order_id DESC
    LIMIT 10;
""")

results = cursor.fetchall()
print("customer_id | order_id")
print("----------------------------")
for row in results:
    print(f"{row[0]}   | {row[1]}")

# 2. Produsele cu cele mai multe recenzii
cursor.execute("""
    SELECT product_id, COUNT(review_id) AS review_id
    FROM reviews
    GROUP BY product_id
    ORDER BY review_id DESC
    LIMIT 10;
""")

results = cursor.fetchall()
print("Cei mai activi clienti (top 10 clienti dupa numarul de comenzi")
print("----------------------------")
for row in results:
    print(f"{row[0]}     | {row[1]}")

top_reviewed_products = cursor.fetchall()
print("\nProdusele cu cele mai multe recenzii:")
for product in top_reviewed_products:
    print(product)

# 3. Categoriile cu cele mai multe vânzări în funcție de cantitate
cursor.execute("""
    SELECT p.category, SUM(o.quantity) AS total_quantity
    FROM orders o
    JOIN products p ON o.product_id = p.product_id
    GROUP BY p.category
    ORDER BY total_quantity DESC
    LIMIT 10;
""")

results = cursor.fetchall()
print("\n Categoriile cu cele mai multe vanzari in functie de cantitate:")
print("----------------------------")
for row in results:
    print(f"{row[0]}        | {row[1]}")