## Dataset Links 
- [Steam Games Dataset (approximately 70k lines)](https://www.kaggle.com/datasets/mexwell/steamgames)
- [Steam Game Reviews Dataset (approximately 500k lines)](https://www.kaggle.com/datasets/andrewmvd/steam-reviews)
- [Steam Game Genres (approximately 25k lines)](https://www.kaggle.com/datasets/danieliusv/steam-games-genres)


>Recommended to run this project in either a native Linux environment or a virtual machine with Linux

## Makefile Instructions  

1. Download the datasets from the kaggle links in the [Dataset Links](#dataset-links) section into the project's directory.
2. Install the project's dependencies by running the command `make install` in the project's directory.
3. To run all of the processes, use the command `make all`. Alternatively, the following specific targets can also be used:
   - `setup`: Install necessary libraries, contained in the *requirements.txt* file, into the project's virtual environment.
   - `export_json`: Takes the *.db* database file, converts and partitions it into *.json* files.
   - `database`: Generate the SQLite3 database from the raw dataset .csv files.
   - `plot`: Create plots from the data in the datasets.
   - `refine`: Refine the datasets.
- The Makefile also includes cleaning targets:
   - `clean_not_needed`: Removes only the *\_\_pycache__* directory and refined dataset files.
   - `clean`: Also removes the plot images and database files.
   - `clean_all`: Removes the virtual environment (*.venv*) directory.


## Solr Instructions

1. Run the command below to create the Solr container and the project's Solr core.
   ```docker
      docker run -p 8983:8983 --name pri_solr -v ${PWD}:/data -d solr:9.3 solr-precreate games
   ```
2. Execute the startup.sh script by using the command
   ```bash
      sh startup.sh
   ```
3. Open this [link](http://localhost:8983) on a web browser (*localhost* on the default Solr port 8983).
