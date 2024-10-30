import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from password import parola

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password=parola,
    database="curs_final"
)
cursor = conn.cursor(dictionary=True)

def fetch_data(query):
    cursor.execute(query)
    return pd.DataFrame(cursor.fetchall())

orders_df = fetch_data("SELECT * FROM orders")
customers_df = fetch_data("SELECT * FROM customers")
products_df = fetch_data("SELECT * FROM products")
reviews_df = fetch_data("SELECT * FROM reviews")

cursor.close()
conn.close()

orders_df['order_value'] = orders_df['quantity'] * orders_df['price']
plt.figure(figsize=(10, 6))
sns.histplot(orders_df['order_value'], bins=30, kde=True)
plt.title("Distribuția valorii comenzilor")
plt.xlabel("Valoare comandă", fontsize=20)
plt.ylabel("Frecvența",fontsize=20)
plt.show()

customers_per_country = customers_df['country'].value_counts()
plt.figure(figsize=(36, 18))
sns.barplot(x=customers_per_country.index, y=customers_per_country.values, palette="coolwarm")
plt.title("Numărul de clienți pe țară",fontsize=40)
plt.xlabel("Țara" , fontsize=20)
plt.ylabel("Numărul de clienți" , fontsize=40)
plt.xticks(rotation=90)
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(x='rating', data=reviews_df, palette="coolwarm")
plt.title("Distribuția ratingurilor", fontsize=20)
plt.xlabel("Rating", fontsize=20)
plt.ylabel("Număr de recenzii", fontsize=20)
plt.show()

products_per_category = products_df['category'].value_counts()
plt.figure(figsize=(12, 6))
sns.barplot(x=products_per_category.index, y=products_per_category.values, palette="coolwarm")
plt.title("Numărul de produse pe categorii", fontsize=20)
plt.xlabel("Categorie", fontsize=20)
plt.ylabel("Număr de produse", fontsize=20)
plt.xticks(rotation=45)
plt.show()
