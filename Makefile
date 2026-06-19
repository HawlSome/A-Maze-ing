MAIN = a_maze_ing.py
CONFIG = config.txt

run:
	@python3 $(MAIN) $(CONFIG)

env:
	@python3 -m venv .venv
	@echo "Run: source .venv/bin/activate.fish"

install:
	@pip install -r requirements.txt


desactivate:
	deactivate

clean:
	@find . -type d -name "*cache*" | xargs rm -rf

lint: 
	@flake8 . --exclude=.venv,__pycache__,.mypy_cache
	@mypy . --warn-return-any --warn-unused-ignore \
	 --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
	@$(MAKE) -s clean