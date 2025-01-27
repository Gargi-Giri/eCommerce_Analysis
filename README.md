# eCommerce_Analysis
# eCommerce Transactions Analysis

This repository contains the solution for analyzing eCommerce transaction data and finding customer lookalikes based on their purchasing behavior. The task is divided into two main parts:

1. **Finding Lookalike Customers:** 
   Using similarity measures to identify customers with similar purchasing behaviors.

2. **Visualizing Customer Clusters:**
   Using clustering techniques (like K-Means) to visualize customer groups based on their purchasing patterns.

## Project Structure

- **`Customers.csv`**: Contains customer data with fields like `CustomerID`, `Name`, `Age`, etc.
- **`Products.csv`**: Contains product details such as `ProductID`, `Name`, `Category`, and `Price`.
- **`Transactions.csv`**: Contains transaction details for each customer, including `TransactionID`, `ProductID`, `Quantity`, `TotalValue`, etc.
- **`Lookalike.csv`**: A CSV file containing the top 3 lookalike customers for each customer, along with the similarity scores.
- **`EDA.py`**: Exploratory Data Analysis (EDA) script to inspect the dataset and perform basic statistics.
- **`validate_lookalikes.py`**: Validates the lookalike recommendations for each customer by checking their transaction history.
- **`visualize_clusters.py`**: Script to generate and visualize customer clusters based on lookalike similarity using PCA and K-means clustering.

## Steps to Run the Code

1. **Set Up the Environment:**

   First, clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/eCommerce_Analysis.git
   cd eCommerce_Analysis
