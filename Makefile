all: json

json: database
	mkdir -p data
	./.venv/bin/python3 export_json.py

database: plot
	./.venv/bin/python3 database.py
#	sqlite3 database.db .dump | gzip -c > database.dump.gz

plot: refine
	./.venv/bin/python3 plot.py

refine: setup
	./.venv/bin/python3 refine.py

setup: requirements.txt
	python3 -m venv .venv
	./.venv/bin/pip install -r requirements.txt

install:
	sudo apt-get install -y python3 python3-virtualenv sqlite3 gzip

clean_all: clean
	rm -rf .venv

clean_not_needed:
	rm -rf __pycache__
	rm -f refined_data/refined_*.csv

clean:
	rm -rf __pycache__
	rm -f refined_data/refined_*.csv images/*.png database.dump.gz db/database.db

.PHONY: clean clean_not_needed clean_all setup refine plot database run install