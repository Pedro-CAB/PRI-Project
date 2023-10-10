# Steam Games Search System
This project is being developed in the Information Processing and Retrieval course, at the first year of the Masters Degree in Computer Engineering and Informatics at FEUP, in the year of 2023. We are developing a search system that contains information about games for sale on Steam based on datasets about those games and user reviews on them.

## Dataset Links 
- [Steam Games Dataset (approximately 70k lines)](https://www.kaggle.com/datasets/mexwell/steamgames)
- [Steam Game Reviews Dataset (approximately 500k lines)](https://www.kaggle.com/datasets/andrewmvd/steam-reviews)
- [Steam Game Genres (approximately 25k lines)](https://www.kaggle.com/datasets/danieliusv/steam-games-genres)

## Other Important Links
- [Overleaf Editable Report](https://www.overleaf.com/project/65158970b4dfdbdf08a7b83f)

## Developed By
- Filipe Fonseca, up202003474@up.pt
- Rita Oliveira, up202004155@up.pt
- Marcelo Apolinário, up201603903@up.pt
- Pedro Gomes, up202006086@up.pt

## Makefile Instructions
1. Install the project's dependencies by running the command `make install` in the project's directory.
2. To run all of the processes, use the command `make all`. Alternatively, the following specific targets can also be used:
   - `setup`: Install necessary libraries, contained in the *requirements.txt* file, into the project's virtual environment.
   - `database`: Generate the SQLite3 database from the raw dataset .csv files.
   - `plot`: Create plots from the data in the datasets.
   - `refine`: Refine the datasets.
- The Makefile also includes cleaning targets:
   - `clean_not_needed`: Removes only the *\_\_pycache__* directory and refined dataset files.
   - `clean`: Also removes the plot images and database files.
   - `clean_all`: Removes the virtual environment (*.venv*) directory.
