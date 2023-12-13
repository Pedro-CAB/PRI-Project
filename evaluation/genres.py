import json

# Load the JSON data from your file
with open('subset.json', 'r') as file:
    data = json.load(file)

# Convert the 'genres' attribute from string to list
data["genres"] = json.loads(data["genres"][0].replace(",", "\",\""))

# Save the modified data back to the file
with open('subset_modified.json', 'w') as file:
    json.dump(data, file, indent=2)
