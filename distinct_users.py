import pandas as pd

# Load the final dataset
final_df = pd.read_csv("final_food_delivery_dataset.csv")

# Count distinct users
distinct_users = final_df['user_id'].nunique()

print("Number of distinct users who placed at least one order:", distinct_users)
