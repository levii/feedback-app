pip-compile:
	pip-compile -o src/requirements.txt src/requirements.in
	pip-compile -o src/requirements.dev.txt src/requirements.txt src/requirements.dev.in

test:
	PYTHONPATH=src pytest -vv tests
