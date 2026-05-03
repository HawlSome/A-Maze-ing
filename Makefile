MAIN = a_maze_ing.py
CONFIG = config.txt

run:
	@python3 $(MAIN) $(CONFIG)

clean:
	@find . -type d -name "*cache*" | xargs rm -rf

lint:
	@flake8 .
	@python -m mypy . --warn-return-any --warn-unused-ignore \
	 --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs