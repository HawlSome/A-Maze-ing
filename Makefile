MAIN = a_maze_ing.py
CONFIG = config.txt

run:
	@python3 $(MAIN) $(CONFIG)

install:
	@pip install flake8
	@pip install mypy

env:
	@python3 -m venv .venv
	@echo "Run: source .venv/bin/activate.fish"

desactivate:
	deactivate

clean:
	@find . -type d -name "*cache*" | xargs rm -rf

lint:
	@flake8 . --exclude=.venv,__pycache__,.mypy_cache
	@mypy . --warn-return-any --warn-unused-ignore \
	 --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs