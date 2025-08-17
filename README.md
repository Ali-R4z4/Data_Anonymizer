📌 Data Anonymizer

This project is a Data Anonymization Tool that applies Differential Privacy and K-Anonymity techniques to protect sensitive information in datasets. It allows users to anonymize numerical and string-based columns through configurable methods.


🔹 Features

Differential Privacy (Laplace Noise): Adds controlled noise to numerical columns (Age, Salary) based on user-defined epsilon values.
K-Anonymity Strategies for String Data:
Suppress: Replaces data with masked values (*****)
Generalize: Masks sensitive details while keeping partial information
Synthetic: Generates realistic but fake data using the Faker library (Name, Location, Phone)

🔹 How It Works

Load the dataset from data/sample_dataset.csv.
User provides epsilon values for numerical columns.
User selects anonymization strategies for string columns.
The tool processes the dataset and saves the anonymized version as data/anonymized_dataset.csv.

🔹 File Structure

main.py → Entry point, takes user input and runs anonymization.
anonymizer.py → Contains anonymization functions (Differential Privacy + K-Anonymity).
data/sample_dataset.csv → Input dataset (replace with your own).
data/anonymized_dataset.csv → Output anonymized dataset.

🔹 How to Run

# Install dependencies
pip install pandas numpy faker

# Run the anonymizer
python main.py
