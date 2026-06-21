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
	@flake8 . --exclude=.venv,__pycache__,.mypy_cache,.env,env
	@mypy . --warn-return-any --warn-unused-ignore \
	 --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs\
	@$(MAKE) -s clean

lint-strict: 
	@flake8 . --exclude=.venv,__pycache__,.mypy_cache,.env,env
	@mypy . --warn-return-any --warn-unused-ignore \
	 --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs\
	 --strict
	@$(MAKE) -s clean

.PHONY: run install debug clean lint lint-strict