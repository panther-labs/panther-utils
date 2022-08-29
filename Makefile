# Targets for local development
install:: utl_activate ci_install
fmt::     install ci_fmt
lint::    fmt ci_lint
test::    fmt ci_lint ci_test

# Targets for CI
ci_install::
	pip3 install -qr dev-requirements.txt

ci_fmt::
	black panther_utils tests

ci_lint::
	mypy --config-file mypy.ini panther_utils tests

ci_test::
	nosetests -v --with-coverage --cover-package=panther_utils --cover-min-percentage=100

# Utility targets
venv:
	python3 -m venv venv

utl_activate: venv
	. venv/bin/activate

publish: utl_activate
	rm -rf dist
	python3 setup.py sdist
	twine upload ./dist/panther_utils-*.tar.gz