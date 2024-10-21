SHELL=/bin/bash

default:	instructions

VENV_DIR=venv

instructions:
	echo "enter valid target (setup, run, clean)"

setup:
	python3 -m venv $(VENV_DIR)
	source $(VENV_DIR)/bin/activate && pip install -r requirements.txt

run:
	source $(VENV_DIR)/bin/activate && python app.py

clean:
	rm -rf $(VENV_DIR)
	find . -name "__pycache__" -type d -exec rm -rf {} +