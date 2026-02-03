import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned data
data = pd.read_csv("data/processed/cleaned_data.csv")

# Create User–Item Interaction Matrix
# Rows = users, Columns = products, Values = interactions
user_item_matrix = data.pivot_table(
    index='user_id',
    columns='product_id',
    values='event_type',
    aggfunc='count',
    fill_value=0
)

# Compute Item–Item Similarity using Cosine Similarity
item_similarity = cosine_similarity(user_item_matrix.T)

# Convert similarity matrix to DataFrame
item_similarity_df = pd.DataFrame(
    item_similarity,
    index=user_item_matrix.columns,
    columns=user_item_matrix.columns
)

# Function to recommend products
def recommend_products(product_id, top_n=5):
    similar_items = item_similarity_df[product_id].sort_values(ascending=False)
    recommended_items = similar_items.iloc[1:top_n+1]
    return recommended_items

# Example Recommendation
sample_product = user_item_matrix.columns[0]
print("Recommended products for product:", sample_product)
print(recommend_products(sample_product))
