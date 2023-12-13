# from transformers import pipeline, AutoTokenizer
import pandas as pd

# # Load the sentiment analysis model
# classifier = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=1)

# # Load the tokenizer for the sentiment analysis model
# tokenizer = AutoTokenizer.from_pretrained("j-hartmann/emotion-english-distilroberta-base")

# # # Read your CSV file into a DataFrame
# games_reviews_df = pd.read_csv("refined_data/sampled_reviews.csv")

# # Define the maximum sequence length
# max_seq_length = 510

# # Define a function to process the text
# def process_text(text):
#     # Tokenize the text
#     tokens = tokenizer.encode(text, max_length=max_seq_length, truncation=True)

#     # Convert the list of tokens to a string
#     processed_text = tokenizer.decode(tokens, skip_special_tokens=True)

#     return processed_text

# print("Processing...")

# # Apply the processing function to each row in the DataFrame
# games_reviews_df['processed_text'] = games_reviews_df['text'].apply(process_text)

# print("Processing done")

# print("Analyzing sentiments...")

# # Apply sentiment analysis to the processed text
# games_reviews_df['sentiment'] = games_reviews_df['processed_text'].apply(lambda x: classifier(x)[0][0]['label'])
# print("\t- Added sentiment column")

# # Drop the intermediate processed_text column if you don't need it
# games_reviews_df = games_reviews_df.drop(columns=['processed_text'])

# # Save the DataFrame to a new CSV file
# games_reviews_df.to_csv("refined_data/refine_reviews.csv", index=False)
# print("Refinement: Refined game reviews")

games_reviews_df = pd.read_csv("refined_data/refine_reviews.csv")
games_df = pd.read_csv("refined_data/refined_games.csv")
games_df.drop(['stemmed', 'tokens'], axis=1, inplace=True)

game_sentiments = games_reviews_df.groupby('app_id')['sentiment'].agg(lambda x: x.value_counts().idxmax()).reset_index()

# Merge the game_sentiments DataFrame with games_df on app_id
games_df = pd.merge(games_df, game_sentiments, on='app_id', how='left')

# Rename the 'sentiment' column to 'player_sentiment'
games_df = games_df.rename(columns={'sentiment': 'player_sentiment'})


games_df.to_csv("refined_data/final_games.csv", index=False)