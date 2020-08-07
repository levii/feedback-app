pip-compile:
	pip-compile -o src/requirements.txt src/requirements.in
	pip-compile -o src/requirements.dev.txt src/requirements.txt src/requirements.dev.in

pip-install:
	pip install -r src/requirements.dev.txt

test:
	PYTHONPATH=src pytest -vv tests
