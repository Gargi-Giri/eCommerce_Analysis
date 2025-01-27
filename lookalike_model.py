import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load data
customers_df = pd.read_csv("Customers.csv")
products_df = pd.read_csv("Products.csv")
transactions_df = pd.read_csv("Transactions.csv")

# Clean column names
customers_df.columns = customers_df.columns.str.strip()
products_df.columns = products_df.columns.str.strip()
transactions_df.columns = transactions_df.columns.str.strip()

# Check if CustomerID exists in all DataFrames
assert 'CustomerID' in customers_df.columns, "CustomerID missing in Customers.csv"
assert 'CustomerID' in transactions_df.columns, "CustomerID missing in Transactions.csv"

# Aggregate transaction data
transaction_features = transactions_df.groupby('CustomerID').agg({
    'TotalValue': 'sum',
    'Quantity': 'sum'
}).reset_index()

# Merge with customer profiles
customer_profiles = pd.merge(customers_df, transaction_features, on='CustomerID', how='left').fillna(0)

# Create a customer-product purchase matrix
product_category_matrix = pd.pivot_table(transactions_df, index='CustomerID', columns='ProductID', values='Quantity', aggfunc='sum', fill_value=0)

# Check if we have enough data for similarity calculation
if product_category_matrix.shape[0] < 2:
    raise ValueError("Not enough customer data for similarity computation.")

# Compute similarity matrix
similarity_matrix = cosine_similarity(product_category_matrix)
customer_indices = list(product_category_matrix.index)

# Function to get top 3 similar customers
def get_lookalikes(customer_id, num_lookalikes=3):
    if customer_id not in customer_indices:
        return []  # No transactions, can't compute similarity
    
    customer_idx = customer_indices.index(customer_id)
    similarity_scores = similarity_matrix[customer_idx]
    
    # Sort and get top similar customers (excluding self)
    similar_indices = np.argsort(similarity_scores)[::-1][1:num_lookalikes+1]
    return [(customer_indices[i], similarity_scores[i]) for i in similar_indices]

# Get lookalikes for the first 20 customers
lookalike_data = []
for customer_id in customers_df['CustomerID'][:20]:
    lookalikes = get_lookalikes(customer_id)
    
    if len(lookalikes) < 3:
        lookalikes += [("N/A", 0)] * (3 - len(lookalikes))  # Pad missing values

    lookalike_data.append([customer_id] + [item for sublist in lookalikes for item in sublist])

# Create and save DataFrame
lookalike_df = pd.DataFrame(lookalike_data, columns=['CustomerID', 'Lookalike_1', 'Similarity_1', 'Lookalike_2', 'Similarity_2', 'Lookalike_3', 'Similarity_3'])
lookalike_df.to_csv('Lookalike.csv', index=False)

# Display first few rows
print(lookalike_df.head())
