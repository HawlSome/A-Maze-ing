MAIN = a_maze_ing.py
CONFIG = config.txt

run:
	@python3 $(MAIN) $(CONFIG)

install:
	@pip install -r requirements.txt

debug:
	@python3 -m pdb $(MAIN) $(CONFIG)

clean:
	@find . -type d -name "*cache*" | xargs rm -rf

lint: 
	@flake8 . --exclude=__pycache__,.mypy_cache,.env,env
	@mypy . --warn-return-any --warn-unused-ignore \
	 --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict: 
	@flake8 . --exclude=__pycache__,.mypy_cache,.env,env
	@mypy . --warn-return-any --warn-unused-ignore \
	 --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs \
	 --strict

.PHONY: run install debug clean lint lint-strict