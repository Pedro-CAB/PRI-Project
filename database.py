import sqlite3
import pandas as pd

def create_connection(db_file):
    """ Create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    connection = None
    try:
        connection = sqlite3.connect(db_file)
        return connection
    except sqlite3.Error as e:
        print(e)

    return connection

def create_table(connection, statement):
    """ Create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = connection.cursor()
        c.execute(statement)
    except sqlite3.Error as e:
        print(e)


def main():
    database = r'db/database.db'

    # create table creation statements
    sql_create_games_table = """
        CREATE TABLE IF NOT EXISTS games (
            app_id          INTEGER PRIMARY KEY,
            name            TEXT,
            release_date    DATE,
            price           DECIMAL,
            about_info      TEXT,
            languages       TEXT,
            windows         BOOLEAN,
            mac             BOOLEAN,
            linux           BOOLEAN,
            meta_score      INTEGER,
            positive        INTEGER,
            negative        INTEGER,
            achievements    INTEGER,
            recommendations INTEGER,
            developers      TEXT,
            publishers      TEXT,
            categories      TEXT,
            genres          TEXT,
            tags            TEXT,
            player_sentiment TEXT
        );
    """
    # create database connection
    connection = create_connection(database)
    print("Database: Database connection established.")

    # create tables
    create_table(connection, sql_create_games_table)

    # add data
    games_df = pd.read_csv('refined_data/final_games.csv')
    cursor = connection.execute('SELECT * FROM games')
    games_cols = [description[0] for description in cursor.description]
    games_df[games_cols].to_sql('games', connection, if_exists='append', index=False)

    print("Database: Database created successfully!")



if __name__ == '__main__':
    main()
