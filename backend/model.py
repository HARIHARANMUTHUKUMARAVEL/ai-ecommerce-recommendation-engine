import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned data
data = pd.read_csv("../data/processed/cleaned_data.csv")

# Create user–item matrix
user_item_matrix = data.pivot_table(
    index="user_id",
    columns="product_id",
    values="event_type",
    aggfunc="count",
    fill_value=0
)

# Compute item similarity
item_similarity = cosine_similarity(user_item_matrix.T)

item_similarity_df = pd.DataFrame(
    item_similarity,
    index=user_item_matrix.columns,
    columns=user_item_matrix.columns
)

def recommend_items(product_id, top_n=5):
    scores = item_similarity_df[product_id].sort_values(ascending=False)
    return scores.iloc[1:top_n+1].index.tolist()
