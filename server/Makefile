pip-compile:
	pip-compile -o src/requirements.txt src/requirements.in
	pip-compile -o src/requirements.dev.txt src/requirements.txt src/requirements.dev.in

pip-install:
	pip install -r src/requirements.dev.txt

mypy:
	mypy src/

black:
	black src/ tests/

flake8:
	flake8 src/ tests/

check: mypy black flake8

test:
	PYTHONPATH=src pytest -vv tests
