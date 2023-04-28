poetry-setup:
	poetry install

.PHONY: run
run:
	poetry run python main.py

.PHONY: export
export:
	poetry export -f requirements.txt --output requirements.txt --without-hashes