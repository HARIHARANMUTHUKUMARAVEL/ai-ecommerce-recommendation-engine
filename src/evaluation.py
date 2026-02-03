import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load cleaned data
data = pd.read_csv("data/processed/cleaned_data.csv")

# Create user–item interaction matrix
user_item_matrix = data.pivot_table(
    index='user_id',
    columns='product_id',
    values='event_type',
    aggfunc='count',
    fill_value=0
)

# Compute item similarity
item_similarity = cosine_similarity(user_item_matrix.T)
item_similarity_df = pd.DataFrame(
    item_similarity,
    index=user_item_matrix.columns,
    columns=user_item_matrix.columns
)

# Recommendation function
def recommend_items(item_id, top_n=5):
    scores = item_similarity_df[item_id].sort_values(ascending=False)
    return scores.iloc[1:top_n+1].index.tolist()

# Precision, Recall, F1 calculation
def evaluate_model(test_users, top_n=5):
    precisions, recalls = [], []

    for user in test_users:
        interacted_items = user_item_matrix.loc[user]
        actual_items = interacted_items[interacted_items > 0].index.tolist()

        if len(actual_items) == 0:
            continue

        recommended_items = recommend_items(actual_items[0], top_n)

        true_positives = len(set(actual_items) & set(recommended_items))

        precision = true_positives / len(recommended_items)
        recall = true_positives / len(actual_items)

        precisions.append(precision)
        recalls.append(recall)

    avg_precision = np.mean(precisions)
    avg_recall = np.mean(recalls)
    f1_score = 2 * (avg_precision * avg_recall) / (avg_precision + avg_recall)

    return avg_precision, avg_recall, f1_score

# Run evaluation
users_sample = user_item_matrix.index[:100]
precision, recall, f1 = evaluate_model(users_sample)

print(f"Precision: {precision:.2f}")
print(f"Recall: {recall:.2f}")
print(f"F1-Score: {f1:.2f}")
