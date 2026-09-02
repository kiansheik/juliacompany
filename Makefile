.PHONY: check test inventory credentials-pgdas

check:
	python3 -m unittest discover -s tests
	python3 scripts/check.py

test:
	python3 -m unittest discover -s tests

inventory:
	python3 scripts/inventory.py

credentials-pgdas:
	python3 scripts/credentials_pgdas.py

push:
	git add .
	git commit
	git push origin HEAD