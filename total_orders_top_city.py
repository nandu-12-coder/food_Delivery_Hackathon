import pandas as pd

final_df = pd.read_csv("final_food_delivery_dataset.csv")

# Filter Gold members
gold_df = final_df[final_df['membership'] == 'Gold']

# Top revenue city
top_city = gold_df.groupby('city')['total_amount'].sum().idxmax()

# Orders in that city
total_orders_top_city = len(gold_df[gold_df['city'] == top_city])

print(f"Top revenue city among Gold members: {top_city}")
print(f"Total orders in {top_city} by Gold members: {total_orders_top_city}")
