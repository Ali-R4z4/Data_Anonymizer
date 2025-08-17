import numpy as np
import pandas as pd
from faker import Faker

faker = Faker()

# --------------- Differential Privacy --------------- #
def apply_differential_privacy(df, numerical_column_config):
    df = df.copy()
    for col, epsilon in numerical_column_config.items():
        if col not in df.columns:
            continue
        sensitivity = df[col].max() - df[col].min()
        scale = sensitivity / epsilon
        noise = np.random.laplace(0, scale, size=len(df))
        df[col] = df[col] + noise
    return df

# --------------- K-Anonymity Strategies --------------- #
def suppress_column(df, column):
    df[column] = '*' * 5  # Suppress data by replacing with 5 stars
    return df

def generalize_column(df, column):
    # Generalize string data by masking everything after the first character
    df[column] = df[column].astype(str).apply(lambda x: x[0] + '*' * (len(x) - 1) if len(x) > 1 else x)
    return df

def synthetic_column(df, column):
    # Use Faker for synthetic replacement based on column type
    if "name" in column.lower():
        df[column] = [faker.name() for _ in range(len(df))]
    elif "location" in column.lower():
        df[column] = [faker.city() for _ in range(len(df))]
    elif "phone" in column.lower():
        df[column] = [faker.phone_number() for _ in range(len(df))]
    else:
        df[column] = [faker.word() for _ in range(len(df))]
    return df

def apply_k_anonymity(df, string_column_config):
    df = df.copy()
    for column, method in string_column_config.items():
        if column not in df.columns:
            continue
        if method == "suppress":
            df = suppress_column(df, column)
        elif method == "generalize":
            df = generalize_column(df, column)
        elif method == "synthetic":
            df = synthetic_column(df, column)
    return df
