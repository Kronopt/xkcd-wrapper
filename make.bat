@echo off

if "%1" == "" goto help
goto %~1

:help
echo.
echo install-dependencies           installs dependencies
echo install-dependencies-dev       installs dev dependencies
echo.
echo test                           runs tests
echo lint                           runs linter
echo coverage                       runs coverage test
echo docs-test                      tests docs for build errors and serves them locally
echo.
echo build                          builds python package (sdist)
echo build-test                     tests build for errors and uploads to test.pypi.org
echo release                        builds and uploads python package to pypi.org
echo.
echo clean-coverage                 removes coverage files
echo clean-build                    removes packaging artifacts
echo clean-pyc                      removes python file artifacts
echo clean                          runs all cleaning functions
echo.
goto:eof

:install-dependencies
python -m pip install -r requirements.txt
goto:eof

:install-dependencies-dev
python -m pip install -r requirements-dev.txt
goto:eof

:test
nose2 -s .\tests -t .
goto:eof

:lint
python -m pylint xkcd_wrapper setup.py
goto:eof

:coverage
python -m coverage run --source xkcd_wrapper -m nose2 -s .\tests -t .
python -m coverage report -m
goto:eof

:docs-test
mkdocs serve -s -f .mkdocs.yml
goto:eof

:build
call:clean-pyc
call:clean-build
python setup.py sdist bdist_wheel
goto:eof

:build-test
twine check dist/*
twine upload --repository-url https://test.pypi.org/legacy/ dist/*
goto:eof

:release
call:build
twine upload dist/*
goto:eof

:clean-coverage
python -m coverage erase
goto:eof

:clean-build
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q xkcd_wrapper.egg-info
goto:eof

:clean-pyc
rmdir /s /q xkcd_wrapper\__pycache__
rmdir /s /q tests\__pycache__
del /s xkcd_wrapper\*.pyc xkcd_wrapper\*.pyo xkcd_wrapper\*~
del /s tests\*.pyc tests\*.pyo tests\*~
goto:eof

:clean
call:clean-coverage
call:clean-build
call:clean-pyc
goto:eof
