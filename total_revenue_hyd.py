import pandas as pd

# Load the final dataset
final_df = pd.read_csv("final_food_delivery_dataset.csv")

# Filter for Hyderabad orders
hyd_orders = final_df[final_df['city'] == 'Hyderabad']

# Sum total_amount and round to nearest integer
total_revenue_hyd = round(hyd_orders['total_amount'].sum())

print("Total revenue from Hyderabad orders:", total_revenue_hyd)
