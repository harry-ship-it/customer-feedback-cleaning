import pandas as pd
import numpy as np
import re

# Load the dataset
data = pd.read_csv('raw_customer_feedback.csv')

print("Original Data:")
print(data.head())

# Step 1: Clear text so that theres no special characters 
def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r'http\S+|www\.\S+', '', text)  # Remove URLs
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)  # Remove special characters
    text = text.strip().lower()  # Convert to lowercase & trim spaces
    return text

data['feedback'] = data['feedback'].apply(clean_text)

# Step 2: Fill in missing data
# Fill missing ratings with median rating
data['rating'] = data['rating'].fillna(data['rating'].median())

# Step 3: Standardize Date Formats
data['date'] = pd.to_datetime(data['date'], errors='coerce')

# Step 4: Remove any duplicate feedback
data = data.drop_duplicates(subset=['feedback'])

# Step 5: Save the new data 
cleaned_file_path = 'cleaned_customer_feedback.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
