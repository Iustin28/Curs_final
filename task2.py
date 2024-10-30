import mysql.connector
import pandas as pd
from datetime import date
from datetime import datetime

from password import parola

my_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password=str(parola),
    database='proiect_final'
)
cursor = my_db.cursor()
# cursor.execute('CREATE DATABASE Proiect_final')

# 2.1

query = 'SELECT * from orders'
df_sales = pd.read_sql(query, my_db)
df_sales['order_date'] = pd.to_datetime(df_sales['order_date'], errors='coerce')
df_sales = df_sales.dropna(subset=['order_date'])
df_sales['revenue'] = df_sales['quantity'] * df_sales['price']
df_sales['year_month'] = df_sales['order_date'].dt.to_period('M')
monthly_revenue = df_sales.groupby('year_month')['revenue'].sum().reset_index()
print(monthly_revenue)

#2.2

query_analiza_produselor_populare = "SELECT o.product_id, p.category, p.stock, o.quantity,p.product_id from orders o JOIN products p ON o.product_id = p.product_id"
df_popular = pd.read_sql(query_analiza_produselor_populare, my_db)
df_populat_grupat = df_popular.groupby('category')['stock'].sum()
print(df_populat_grupat)

#2.3

query_valoare_totala_a_clientilor = "SELECT o.customer_id, c.customer_id,c.name, o.price, o.quantity from orders o JOIN customers c ON o.customer_id = c.customer_id"
df_clienti = pd.read_sql(query_valoare_totala_a_clientilor, my_db)
print(df_clienti)
suma_clienti = df_clienti.groupby('name')['price'].sum()
print(suma_clienti)


#2.4
query_rating = "SELECT product_id,avg(rating) FROM reviews group by product_id order by product_id;"
df_rating = pd.read_sql(query_rating, my_db)
print(df_rating)

#2.5

query_top_clientilor = "SELECT o.customer_id, count(c.customer_id),c.name from orders o JOIN customers c ON o.customer_id = c.customer_id group by c.customer_id order by c.customer_id"
df_clienti = pd.read_sql(query_top_clientilor, my_db)
print(df_clienti.head())