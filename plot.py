import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns
#from nltk.corpus import stopwords
#from nltk.tokenize import word_tokenize
#from nltk.stem import WordNetLemmatizer
#from nltk import ngrams
#from collections import Counter

pd.set_option("display.max_columns", None)
pd.set_option("display.max_rows", None)

def plot_games_release_dates():
    # Read .csv
    games_df = pd.read_csv("refined_games.csv")

    # Convert data type to 'int' and keep only the release year
    games_df["release_date"] = pd.to_datetime(games_df["release_date"], format='mixed').dt.strftime('%Y').astype('int64')

    # Create series to plot
    min_year = games_df["release_date"].min()
    #max_year = games_df["Release date"].max()
    release_year_series = games_df.groupby(pd.cut(games_df["release_date"], np.arange(min_year, 2023, 3)), observed=False).count()["app_id"]

    # Configure plot
    plt.rcParams.update({"font.size": 18})
    plt.ylabel("No. of Games")
    plt.title("Games released per year")

    # Create plot
    release_year_series.plot.bar()

    # Save plot as an image file
    fig = plt.gcf()
    fig.set_size_inches(22.5, 18.5)
    fig.savefig('games_released_per_year.png')
    plt.clf()


def plot_games_by_genre():
    # Read .csv
    game_genres_df = pd.read_csv("refined_games_genres.csv")

    # Create series to plot
    games_genre_series = game_genres_df.groupby(game_genres_df["Genre"]).count()['appid']
    genre_dict = dict()

    for (genre, num_games) in games_genre_series.items():
        genres_list = genre.split(", ")
        for genre in genres_list:
            if genre in genre_dict:
                genre_dict[genre] += num_games
            else:
                genre_dict[genre] = num_games

    new_genre_dict = dict()
    new_genre_dict["others"] = 0
    for genre in list(genre_dict):
        if genre_dict[genre] < 1000:
            new_genre_dict["others"] += genre_dict[genre]
            genre_dict.pop(genre, None)
        else:
            new_genre_dict[genre] = genre_dict[genre]

    genre_dict = new_genre_dict
    games_genre_series = pd.Series(genre_dict)

    # Configure plot
    plt.rcParams.update({"font.size": 20})
    plt.ylabel("")
    plt.title("Game Genres")

    # Create plot
    games_genre_series.plot.pie()

    # Save plot as an image
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    fig.savefig("game_genres.png")
    plt.clf()


plots = [plot_games_release_dates,
         plot_games_by_genre]

for i, plot in enumerate(plots):
    print(f'Plotting: {plot.__name__} - {i+1} of {len(plots)}')
    plot()
