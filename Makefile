.PHONY: runserver migrate makemigrations run-migrate

PYTHON = python3
MANAGE = $(PYTHON) manage.py

runserver:
	$(MANAGE) runserver

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

run-migrate:
	$(MAKE) makemigrations && $(MAKE) migrate