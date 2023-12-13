import os
import json
from sentence_transformers import SentenceTransformer

# Load the SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

def get_embedding(text):
    # The model.encode() method already returns a list of floats
    return model.encode(text, convert_to_tensor=False).tolist()

def embed_games(input_files):
    print("Embedding...")
    for input_file in input_files:
        with open(input_file, "r") as f:
            data = json.load(f)
        for document in data:
            name = document.get("name", "")
            about_info = document.get("about_info", "")
            genres = document.get("genres", "")
            tags = document.get("tags", "")
            price = document.get("price", "")
            languages = document.get("languages", "")
            release_date = document.get("release_date", "")
            developers = document.get("developers", "")
            player_sentiment = document.get("player_sentiment", "")
            combined = f"{name} {about_info} {genres} {tags} {price} {languages} {release_date} {developers} {player_sentiment}"
            document["vector"] = get_embedding(combined)

        output_directory = "../semantic_data"
        os.makedirs(output_directory, exist_ok=True)
        output_file = os.path.join(output_directory, os.path.basename(input_file).replace(".json", "_semantic.json"))
        with open(output_file, "w") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Embedded {input_file}")
    print("Finished Embedding!")
file_paths = [f"../data/data{i}.json" for i in range(4)]
embed_games(file_paths[:4])