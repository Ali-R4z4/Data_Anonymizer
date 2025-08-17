import pandas as pd
from anonymizer import apply_differential_privacy, apply_k_anonymity

# Load original dataset
df = pd.read_csv("data/sample_dataset.csv")

# ---- USER CONFIGURATION ---- #

# 1. Get user input for differential privacy (epsilon values for numerical columns)
numerical_columns = ['Age', 'Salary']
numerical_column_config = {}

for col in numerical_columns:
    epsilon = float(input(f"Enter privacy level (epsilon) for '{col}' (e.g., 1.0): "))
    numerical_column_config[col] = epsilon

# 2. Get user input for K-anonymity strategies for string columns
string_column_config = {}
string_columns = ['Name', 'Location', 'Phone']

for column in string_columns:
    print(f"\nSelect an anonymization method for column '{column}':")
    print("1. Suppress")
    print("2. Generalize")
    print("3. Synthetic")
    method_choice = input("Enter the number for your choice (1, 2, or 3): ")

    if method_choice == '1':
        string_column_config[column] = 'suppress'
    elif method_choice == '2':
        string_column_config[column] = 'generalize'
    elif method_choice == '3':
        string_column_config[column] = 'synthetic'
    else:
        print(f"Invalid choice. Defaulting to 'suppress' for '{column}'.")
        string_column_config[column] = 'suppress'

# ---- PROCESSING ---- #

# Apply differential privacy
df = apply_differential_privacy(df, numerical_column_config)

# Apply K-anonymity
df = apply_k_anonymity(df, string_column_config)

# Save result
df.to_csv("data/anonymized_dataset.csv", index=False)
print("✅ Data anonymized successfully. Check 'data/anonymized_dataset.csv'.")
