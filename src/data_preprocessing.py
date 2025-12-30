import pandas as pd

# Load Kaggle dataset (use sample rows)
data = pd.read_csv("data/raw/ecommerce.csv", nrows=100000)

# Select useful columns
data = data[['user_id', 'product_id', 'category_id', 'event_type', 'price']]

# Remove missing values
data.dropna(inplace=True)

# Convert categorical columns to numeric
data['user_id'] = data['user_id'].astype('category').cat.codes
data['product_id'] = data['product_id'].astype('category').cat.codes
data['category_id'] = data['category_id'].astype('category').cat.codes
data['event_type'] = data['event_type'].astype('category').cat.codes

# Save cleaned dataset
data.to_csv("data/processed/cleaned_data.csv", index=False)

print("Milestone-1 Data Preparation Completed Successfully")
