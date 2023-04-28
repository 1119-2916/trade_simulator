poetry-setup:
	poetry install

.PHONY: format
format:
	poetry run isort .
	poetry run black .
	poetry run pflake8 .

.PHONY: run
run:
	poetry run python main.py

.PHONY: export
export:
	poetry export -f requirements.txt --output requirements.txt --without-hashes
