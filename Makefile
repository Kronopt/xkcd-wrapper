.PHONY: help install-dependencies install-dependencies-dev test lint coverage docs-test build build-test release clean clean-pyc clean-coverage clean-build

help:
	@echo ""
	@echo "install-dependencies         installs dependencies"
	@echo "install-dependencies-dev     installs dev dependencies"
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
	@echo "clean-coverage               removes coverage files"
	@echo "clean-build                  removes packaging artifacts"
	@echo "clean-pyc                    removes python file artifacts"
	@echo "clean                        runs all cleaning functions"
	@echo ""

install-dependencies:
	python -m pip install -r requirements.txt

install-dependencies-dev:
	python -m pip install -r requirements-dev.txt

test:
	nose2 -s ./tests -t .

lint:
	python -m pylint xkcd_wrapper setup.py

coverage:
	python -m coverage run --source xkcd_wrapper -m nose2 -s ./tests -t .
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

clean-coverage:
	python -m coverage erase

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf xkcd_wrapper.egg-info/

clean-pyc:
	rm -rf xkcd_wrapper/__pycache__ tests/__pycache__
	rm -f xkcd_wrapper/*.pyc tests/*.pyc
	rm -f xkcd_wrapper/*.pyo tests/*.pyo
	rm -f xkcd_wrapper/*~ tests/*~

clean: clean-coverage clean-build clean-pyc
