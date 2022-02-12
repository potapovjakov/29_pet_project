style:
	flake8 yatinder

types:
	mypy yatinder

test:
	pytest -q

check:
	make test style types

lock:
	pip-compile --generate-hashes --no-emit-index-url
	pip-compile --generate-hashes --no-emit-index-url requirements_dev.in

install:
	pip-sync requirements.txt requirements_dev.txt

install-hooks:
	pre-commit install -t pre-commit -t commit-msg -t pre-push

migrations-check:
	python yatinder/manage.py makemigrations --dry-run --check
