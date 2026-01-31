# Step 0: Import libraries
import pandas as pd
import sqlite3
import os

# Step 1: Check current folder and files
print("Current working directory:", os.getcwd())
print("Files in folder:", os.listdir())
print("-"*60)

# Step 2: Load orders.csv
orders = pd.read_csv("orders.csv")
print("Orders data loaded. Total rows:", len(orders))
print(orders.head())   # first 5 rows
print(orders.tail())   # last 5 rows
print("-"*60)

# Step 3: Load users.json
users = pd.read_json("users.json")
print("Users data loaded. Total rows:", len(users))
print(users.head())
print(users.tail())
print("-"*60)

# Step 4: Load restaurants.sql into SQLite
conn = sqlite3.connect("restaurants.db")
cursor = conn.cursor()

# Drop table if it exists to avoid errors
cursor.execute("DROP TABLE IF EXISTS restaurants")

# Read and execute SQL script
with open("restaurants.sql", "r") as file:
    sql_script = file.read()

cursor.executescript(sql_script)
conn.commit()

# Read restaurants table into pandas
restaurants = pd.read_sql("SELECT * FROM restaurants", conn)
print("Restaurants data loaded. Total rows:", len(restaurants))
print(restaurants.head())
print(restaurants.tail())
print("-"*60)

# Step 5: Merge orders + users (LEFT JOIN)
orders_users = pd.merge(
    orders,
    users,
    on="user_id",
    how="left"
)
print("After merging orders with users. Total rows:", len(orders_users))
print(orders_users.head())
print("-"*60)

# Step 6: Merge with restaurants (LEFT JOIN)
final_df = pd.merge(
    orders_users,
    restaurants,
    on="restaurant_id",
    how="left"
)
print("After merging with restaurants. Total rows:", len(final_df))
print(final_df.head())
print(final_df.tail())
print("-"*60)

# Step 7: Save final dataset
final_df.to_csv("final_food_delivery_dataset.csv", index=False)
print("Final dataset saved as 'final_food_delivery_dataset.csv'")
