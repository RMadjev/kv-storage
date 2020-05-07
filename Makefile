default: help

.PHONY: flake8
lint:
	@flake8 --exclude=.venv core storage

.PHONY: test
test:
	@python3 -m unittest discover -s tests

.PHONY: coverage
coverage:
	@coverage run --omit=.venv/*,/usr/* -m unittest discover && coverage report

.PHONY: help
help:
	@echo 'Usage: make [command]'
	@echo ''
	@echo 'Available commands:'
	@echo ''
	@echo '  flake8           - Check code style with flake8 linter'
	@echo '  test             - Run tests'
	@echo '  coverage         - Generate code coverage'
	@echo '  help             - Default. Show this help message'
