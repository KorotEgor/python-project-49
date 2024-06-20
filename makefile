package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

lint:
	poetry run flake8 brain_games

reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl

