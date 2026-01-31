import pandas as pd

# Load the final dataset
final_df = pd.read_csv("final_food_delivery_dataset.csv")

# Filter orders for restaurants with rating >= 4.5
high_rating_orders = final_df[final_df['rating'] >= 4.5]

# Count total orders
total_high_rating_orders = len(high_rating_orders)

print("Total orders for restaurants with rating >= 4.5:", total_high_rating_orders)
