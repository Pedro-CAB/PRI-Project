import pandas as pd
import nltk
from langdetect import detect
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# Fetch datasets
games_df = pd.read_csv("games.csv")
games_genres_df = pd.read_csv("games_genres.csv")
games_reviews_df = pd.read_csv("games_reviews.csv")
games_reviews_df.rename(columns={"app_id": "AppID"}, inplace=True)

# Finds games with no reviews and returns the games_df without those games
def games_with_reviews():
    merged_df = games_df.merge(games_reviews_df, on='AppID', how='left')
    missing_reviews = merged_df[pd.isna(merged_df['review_text'])]
    new_games_df = games_df[~games_df['AppID'].isin(missing_reviews['AppID'])]

    return new_games_df.reset_index(drop=True)

def review_chars():
    review_lengths = games_reviews_df['review_text'].str.len()
    Q1 = review_lengths.quantile(0.25)
    average_chars = review_lengths.mean()
    Q3 = review_lengths.quantile(0.75)

    print(f"Q1 (25th percentile): {Q1:.2f} characters")
    print(f"The average number of characters in the 'review_text' column is: {average_chars:.2f}")
    print(f"Q3 (75th percentile): {Q3:.2f} characters")

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

### Refine games table
print("Refinement: Refining games table...")
# Remove games without reviews
games_df = games_with_reviews()
print("\t- Deleted games without reviews")

# Remove irrelevant columns
games_df.drop(columns=['Estimated owners', 'Average playtime forever','Median playtime forever','DLC count','Peak CCU','Required age','Average playtime two weeks','Median playtime two weeks','User score', 'Movies', 'Screenshots', 'Notes', 'Score rank', 'Metacritic url', 'Support email', 'Support url', 'Website', 'Reviews', 'Header image', 'Full audio languages'], inplace=True)
print("\t- Removed irrelevant columns")

# Remove duplicate rows
games_df = games_df.drop_duplicates()
print("\t- Removed duplicates")

# Drop null values
games_df = games_df.dropna(subset=['About the game'])
print("\t- Dropped rows with null values")

# Fill null values with NA
games_df.fillna("NA", inplace=True)

# Tokenization and Stemming (no stopwords)
games_df['Tokens'] = games_df['About the game'].apply(lambda text: word_tokenize(text))
games_df['Stemmed'] = games_df['Tokens'].apply(stem_text)
games_df['Stemmed'] = games_df['Stemmed'].apply(remove_stopwords)
print("\t- Tokenized 'About the game' section")

# Format date
games_df['Release date'] = games_df['Release date'].apply(parse_custom_date)
print("\t- Formatted the dates")

# Rename columns (for database implementation)
games_df.rename(columns={
    "AppID": "app_id", "Name": "name", "Release date": "release_date",
    "Price": "price", "About the game": "about_info", "Supported languages": "languages",
    "Windows": "windows", "Mac": "mac", "Linux": "linux",
    "Metacritic score": "meta_score", "Positive": "positive", "Negative": "negative",
    "Achievements": "achievements", "Recommendations": "recommendations",
    "Developers": "developers", "Publishers": "publishers",
    "Categories": "categories", "Genres": "genres", "Tags": "tags",
    "Tokens": "tokens", "Stemmed": "stemmed"}, inplace=True)
print("\t- Renamed columns")

# Save the refined dataset
games_df.to_csv("refined_games.csv", index=False)
print("Refinement: Refined games table")

### Refine game genres table
print("Refinement: Refining game genres table...")
games_genres_df.to_csv("refined_games_genres.csv", index=False)
print("Refinement: Refined game genres table")

### Refine game reviews table
print("Refinement: Refining game reviews...")
# Remove irrelevant columns
games_reviews_df.drop(columns=['app_name'], inplace=True)
print("\t- Removed irrelevant columns")

# Remove duplicate rows
games_reviews_df = games_reviews_df.drop_duplicates()
print("\t- Removed duplicates")

# Drop null values
games_reviews_df = games_reviews_df.dropna(subset=['review_text'])
print("\t- Dropped rows with null values")

# Add an index column
games_reviews_df.reset_index(inplace=True)
print("\t- Added index column")
# Rename columns (for database implementation)
games_reviews_df.rename(columns={
    "AppID": "app_id", "review_text": "text", "review_score": "score",
    "review_votes": "votes", "index": "review_id"}, inplace=True)
print("\t- Renamed columns")

# Save the refined dataset
games_reviews_df.to_csv("refined_games_reviews.csv", index=False)
print("Refinement: Refined game reviews")