import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.metrics.pairwise import cosine_similarity

# Load transaction data
transactions_df = pd.read_csv("Transactions.csv")

# Create product-category matrix
product_category_matrix = pd.pivot_table(transactions_df, index='CustomerID', 
                                         columns='ProductID', values='Quantity', 
                                         aggfunc='sum', fill_value=0)

# Compute similarity
similarity_matrix = cosine_similarity(product_category_matrix)

# Heatmap visualization
sns.heatmap(pd.DataFrame(similarity_matrix, index=product_category_matrix.index, columns=product_category_matrix.index),
            cmap="coolwarm", annot=False)
plt.title("Customer Similarity Heatmap")
plt.show()

# Clustering visualization
linked = linkage(similarity_matrix, method='ward')
plt.figure(figsize=(10, 5))
dendrogram(linked, labels=product_category_matrix.index, leaf_rotation=90)
plt.title("Customer Clustering Dendrogram")
plt.show()
