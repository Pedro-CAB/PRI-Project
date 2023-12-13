import json
import sqlite3

MAX_DATA_SIZE = 2000

def fetch_games(connection):
    query = """SELECT * FROM games"""
    cursor = connection.execute(query)
    result = cursor.fetchall()

    games = list()
    for game in result:
        game = dict(game)
        game["data_type"] = "game"
        games.append(game)

    return games
    

def fetch_game_reviews(connection):
    query = """SELECT * from reviews"""
    cursor = connection.execute(query)
    result = cursor.fetchall()

    reviews = []
    for review in result:
        review = dict(review)
        review["data_type"] = "review"
        reviews.append(review)

    return reviews



try:
    connection = sqlite3.connect('db/database.db')
    connection.row_factory = sqlite3.Row
    print("Export: Database connection established")

    data = list()
    file_num = 0
    games = fetch_games(connection)
    print("Export: Joining in JSON format...")

    for game in games:
        data.append(game)
        
        if len(data) >= MAX_DATA_SIZE:
            with open('data/data%d.json' % file_num, 'w') as fout:
                json.dump(data, fout, indent=2)
                data = []
                file_num += 1

    with open('data/data%d.json' % file_num, 'w') as fout:
        json.dump(data, fout, indent=2)

    print("Export: Finished exporting data.")

except sqlite3.Error as e:
    print("Export: Error while connecting to sqlite database: ", e)

finally:
    if connection:
        connection.close()
        print("Export: Connection closed.")