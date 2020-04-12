# Contributing
<small description>

### Reporting Bugs
Report bugs in the [issues section](<link to issues>).

* Operating system name and version.
* <Project/script name> version.
* Local setup and environment details that might be helpful in troubleshooting.
* Detailed steps to reproduce the bug.

### Fixing Bugs
Look through the [issues section](<link to issues>) for bugs. Anything tagged with `bug`
is open to whoever wants to fix it.

### Implementing Features
Look through the [issues section](<link to issues>) for features. Anything tagged with `feature`
is open to whoever wants to implement it.

When proposing a feature:

* Explain in detail how it would work.
* Keep the scope as narrow as possible, to make it easier to implement.

### Writing Documentation
<small description>

### Submitting Feedback
The best way to send feedback is to open an issue in the [issues section](<link to issues>).

### Get Started!
<detailed steps on how to setup the Project/script

* Fork/download repo from github
* Clone locally / download the repo
* Install into a virtual environment (manually or through an IDE)
    ```
    $ mkdir venv
    $ virtualenv venv/<Project/script name>
    $ cd venv/<Project/script name>/bin
    $ source activate
    $ pip install -r requirements.txt -r requirements-dev.txt
    ```
* Create branch for local development
* Make changes
* Test with pylint, coverage, tox and unittest
* commit changes and push branch to github
* submit a pull request

### Pull Request Guidelines
<minimum requirements needed before submiting a pull request>

* Include tests (if necessary)
* If new functionality is added, the docs should be updated
* Should work on the supported python versions
