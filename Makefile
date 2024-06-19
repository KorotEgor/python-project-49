package-install:
	python3 -m pip install --user dist/*.whl

build:
	poetry build

publish:
	poetry publish --dry-run

