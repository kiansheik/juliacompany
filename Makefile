.PHONY: check test inventory

check:
	python3 -m unittest discover -s tests
	python3 scripts/check.py

test:
	python3 -m unittest discover -s tests

inventory:
	python3 scripts/inventory.py
