packages = panther_utils


deps:
	pipenv install --dev

deps-update:
	pipenv update
	pipenv lock -r  > requirements.txt

lint:
	pipenv run mypy $(packages) --disallow-untyped-defs --ignore-missing-imports --warn-unused-ignores

fmt:
	pipenv run isort --profile=black $(packages)
	pipenv run black --line-length=100 $(packages)

install:
	pipenv install --dev
	pipenv lock -r  > requirements.txt

package-clean:
	rm -rf dist
	rm -f MANIFEST

package: package-clean install test lint
	pipenv run python3 setup.py sdist

publish: install package
	twine upload dist/*

test:
	pipenv run nosetests -v
