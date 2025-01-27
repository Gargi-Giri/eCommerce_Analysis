import pandas as pd

# Load lookalike and transaction data
lookalike_df = pd.read_csv("Lookalike.csv")
transactions_df = pd.read_csv("Transactions.csv")

# Select a sample customer for validation
customer_id = "C0001"  # Change to any CustomerID
lookalike_1 = lookalike_df.loc[lookalike_df['CustomerID'] == customer_id, 'Lookalike_1'].values[0]

# Retrieve transactions of customer & lookalike
customer_transactions = transactions_df[transactions_df["CustomerID"] == customer_id]
lookalike_transactions = transactions_df[transactions_df["CustomerID"] == lookalike_1]

# Print results
print(f"Transactions for {customer_id}:\n", customer_transactions)
print(f"Transactions for lookalike {lookalike_1}:\n", lookalike_transactions)
print(lookalike_df.head())  # This should print the first few lookalikes
