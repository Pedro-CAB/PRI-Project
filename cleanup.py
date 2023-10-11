# Data Cleaning Step

import pandas as pd
import nltk
from langdetect import detect
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Helper functions

# Finds games with no reviews and returns the games_df without those games
def games_with_reviews():
    merged_df = games_df.merge(reviews_df, on='AppID', how='left')
    missing_reviews = merged_df[pd.isna(merged_df['review_text'])]
    new_games_df = games_df[~games_df['AppID'].isin(missing_reviews['AppID'])]

    return new_games_df.reset_index(drop=True)

def review_chars():
    review_lengths = reviews_df['review_text'].str.len()
    Q1 = review_lengths.quantile(0.25)
    average_chars = review_lengths.mean()
    Q3 = review_lengths.quantile(0.75)

    print(f"Q1 (25th percentile): {Q1:.2f} characters")
    print(f"The average number of characters in the 'review_text' column is: {average_chars:.2f}")
    print(f"Q3 (75th percentile): {Q3:.2f} characters")\
    
def remove_stopwords(tokens):
    stop_words = set(stopwords.words('english'))
    return [token for token in tokens if token.lower() not in stop_words]

def stem_text(tokens):
    stemmer = PorterStemmer()
    return [stemmer.stem(token) for token in tokens]

def is_english(text):
    try:
        return detect(text) == 'en'
    except:
        return False
    
def parse_custom_date(date_str):
    try:
        return pd.to_datetime(date_str, format="%b %d, %Y")
    except ValueError:
        try:
            return pd.to_datetime(date_str, format="%b %Y")
        except ValueError:
            return None



games_df = pd.read_csv("data/games.csv")
reviews_df = pd.read_csv("data/reviews.csv")


# Remove games without reviews
games_df = games_with_reviews()
print("Deleted games without reviews")


# Remove irrelevant columns
games_df.drop(columns=['Average playtime forever','Median playtime forever','DLC count','Peak CCU','Required age','Average playtime two weeks','Median playtime two weeks','User score', 'Movies', 'Screenshots', 'Notes', 'Score rank', 'Metacritic url', 'Support email', 'Support url', 'Website', 'Reviews', 'Header image', 'Full audio languages'], inplace=True)
reviews_df.drop(columns=['app_name'])
print("Removed irrelevant columns")


# Remove duplicate rows
#review_chars()
games_df = games_df.drop_duplicates()
reviews_df = reviews_df.drop_duplicates()
print("Removed duplicates")


# Drop null values
reviews_df = reviews_df.dropna(subset=['review_text'])
games_df = games_df.dropna(subset=['About the game'])
print("Dropped rows with Null")

# Fill null values with NA
games_df.fillna("NA", inplace=True)

# Tokenization and Stemming (no stopwords)
games_df['Tokens'] = games_df['About the game'].apply(lambda text: word_tokenize(text))
games_df['Stemmed'] = games_df['Tokens'].apply(stem_text)
games_df['Stemmed'] = games_df['Stemmed'].apply(remove_stopwords)
print("Tokenized About the game section")
# reviews_df['Tokens'] = reviews_df['review_text'].apply(lambda text: word_tokenize(text))
# reviews_df['Stemmed'] = reviews_df['Tokens'].apply(stem_text)
# reviews_df['Stemmed'] = reviews_df['Stemmed'].apply(remove_stopwords)
# print("Tokenized Review text section")

# Remove reviews/games that are not in english
# reviews_df['review_text'] = reviews_df['review_text'].apply(is_english)
games_df['About the game'] = games_df['About the game'].apply(is_english)
print("Only english games/reviews")

# Format date
games_df['Release date'] = games_df['Release date'].apply(parse_custom_date)
print("Formatted the dates")


# Save the Processed Data
games_df.to_csv('cleanData/processed_games.csv', index=False)
reviews_df.to_csv('cleanData/processed_reviews.csv', index=False)
