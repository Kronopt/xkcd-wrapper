.PHONY: help install-dependencies install-dependencies-test test lint coverage docs-test build build-test release clean clean-pyc clean-tests clean-coverage clean-build

help:
	@echo ""
	@echo "install-dependencies         installs dependencies"
	@echo "install-dependencies-test    installs dependencies for testing"
	@echo ""
	@echo "test                         runs tests"
	@echo "lint                         runs linter"
	@echo "coverage                     runs coverage test"
	@echo "docs-test                    tests docs for build errors and serves them locally"
	@echo ""
	@echo "build                        builds python package (sdist)"
	@echo "build-test                   tests build for errors and uploads to test.pypi.org"
	@echo "release                      builds and uploads python package to pypi.org"
	@echo ""
	@echo "clean-tests                  removes temp test files and folders"
	@echo "clean-coverage               removes coverage files"
	@echo "clean-build                  removes packaging artifacts"
	@echo "clean-pyc                    removes python file artifacts"
	@echo "clean                        runs all cleaning functions"
	@echo ""

install-dependencies:
	python -m pip install -r requirements.txt

install-dependencies-test:
	python -m pip install -r requirements-dev.txt

test:
	python -m unittest <tests folder>

lint:
	python -m pylint <project_folder_name> setup.py

coverage:
    python -m coverage run --source <project_folder_name> -m unittest <tests folder>
    python -m coverage report -m

docs-test:
	mkdocs serve -s -f .mkdocs.yml

build: clean-pyc clean-build
	python setup.py sdist bdist_wheel

build-test:
	twine check dist/*
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*

release: build
	twine upload dist/*

clean-tests:
	rm -rf .pytest_cache/

clean-coverage:
	python -m coverage erase

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf <project_folder_name>.egg-info/

clean-pyc:
	rm -rf <project_folder_name>/__pycache__ tests/__pycache__
	rm -f <project_folder_name>/*.pyc tests/*.pyc
	rm -f <project_folder_name>/*.pyo tests/*.pyo
	rm -f <project_folder_name>/*~ tests/*~

clean: clean-tests clean-coverage clean-build clean-pyc
