import pandas as pd

# Load the final dataset
final_df = pd.read_csv("final_food_delivery_dataset.csv")

# Count total orders for Gold members
gold_orders_count = len(final_df[final_df['membership'] == 'Gold'])

print("Total orders placed by Gold users:", gold_orders_count)
