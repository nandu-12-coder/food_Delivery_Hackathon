import pandas as pd

# Load the final dataset
final_df = pd.read_csv("final_food_delivery_dataset.csv")

# Filter for Gold members
gold_orders = final_df[final_df['membership'] == 'Gold']

# Calculate average order value
avg_order_value_gold = round(gold_orders['total_amount'].mean(), 2)

print("Average order value for Gold members:", avg_order_value_gold)
