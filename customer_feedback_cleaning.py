import pandas as pd
import numpy as np
import re

# Load the dataset
data = pd.read_csv('raw_customer_feedback.csv')

# Quick preview of the original data
print("Original Data Sample:")
print(data.head())

# Function to clean up text by removing URLs, special characters, and extra spaces
def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r'http\S+|www\.\S+', '', text)  # Strip URLs
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)  # Keep only alphanumeric and spaces
    return text.strip().lower()

data['feedback'] = data['feedback'].apply(clean_text)

# Fill missing ratings with the median to maintain consistency
if 'rating' in data.columns:
    median_rating = data['rating'].median()
    data['rating'] = data['rating'].fillna(median_rating)

# Parse and standardize dates; set invalid ones to NaT
if 'date' in data.columns:
    data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Remove duplicate feedback entries to ensure unique observations
data = data.drop_duplicates(subset=['feedback'])

# Save the cleaned dataset for downstream use
cleaned_file_path = 'cleaned_customer_feedback.csv'
data.to_csv(cleaned_file_path, index=False)
print(f"Cleaned data has been saved to {cleaned_file_path}")
