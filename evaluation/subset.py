import os
import json
import random

# Function to load a JSON file
def load_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

# Function to save data to a JSON file
def save_json(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

# Get the current script directory
script_dir = os.path.dirname(os.path.realpath(__file__))

# Specify the data directory path (located at the same level as 'evaluation')
data_dir = os.path.join(script_dir, '..', 'data')

# List to store data from all files
all_data = []

# Load data from each file in the data directory
for i in range(4):
    file_path = os.path.join(data_dir, f'data{i}.json')
    print(f"Attempting to load file: {file_path}")  # Add this line
    data = load_json(file_path)
    all_data.extend(data)

# Shuffle the combined data randomly
random.shuffle(all_data)

# Select the first 100 entries
subset_data = all_data[:100]

# Specify the subset file path
subset_file_path = os.path.join(script_dir, 'subset.json')

# Save the subset to a new file called subset.json
save_json(subset_file_path, subset_data)

print("Subset of data saved to subset.json")
