.PHONY: runserver migrate makemigrations run-migrate

PYTHON = python
MANAGE = $(PYTHON) manage.py

runserver:
	$(MANAGE) runserver

makemigrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

run-migrate:
	$(MAKE) makemigrations && $(MAKE) migrate