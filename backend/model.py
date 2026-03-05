import pandas as pd
import random
from sklearn.metrics.pairwise import cosine_similarity

# ==============================
# LOAD DATA
# ==============================

data = pd.read_csv("../data/processed/cleaned_data.csv")

# ------------------------------
# LIMIT DATA SIZE (Memory Safe)
# ------------------------------

TOP_K_PRODUCTS = 1000

top_products = (
    data["product_id"]
    .value_counts()
    .head(TOP_K_PRODUCTS)
    .index
)

data = data[data["product_id"].isin(top_products)]

# ==============================
# ENCODING PRODUCT IDS
# ==============================

original_product_ids = data["product_id"].unique()

product_id_mapping = {pid: idx for idx, pid in enumerate(original_product_ids)}
reverse_product_id_mapping = {idx: pid for pid, idx in product_id_mapping.items()}

data["product_id"] = data["product_id"].map(product_id_mapping)

# ==============================
# USER-ITEM MATRIX
# ==============================

user_item_matrix = data.pivot_table(
    index="user_id",
    columns="product_id",
    values="event_type",
    aggfunc="count",
    fill_value=0
)

# ==============================
# ITEM SIMILARITY MATRIX
# ==============================

item_similarity = cosine_similarity(user_item_matrix.T)

item_similarity_df = pd.DataFrame(
    item_similarity,
    index=user_item_matrix.columns,
    columns=user_item_matrix.columns
)

# ==============================
# RECOMMENDATION FUNCTION
# ==============================

def recommend_items(original_product_id, top_n=5):

    # If product not found → return random products
    if original_product_id not in product_id_mapping:
        all_products = list(reverse_product_id_mapping.values())
        random.shuffle(all_products)
        return [int(x) for x in all_products[:top_n]]

    encoded_id = product_id_mapping[original_product_id]

    # Get similarity scores
    scores = item_similarity_df[encoded_id].sort_values(ascending=False)

    # Take more candidates for diversity
    candidate_encoded = scores.iloc[1:50].index.tolist()

    # Shuffle for variation
    random.shuffle(candidate_encoded)

    # Convert back to original product IDs
    final_recommendations = [
        int(reverse_product_id_mapping[i])
        for i in candidate_encoded[:top_n]
    ]

    return final_recommendations
