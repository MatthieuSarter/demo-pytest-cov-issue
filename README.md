This is a sample repo to reproduce an issue that seems to affect pytest-cov when:
* branch coverage in enabled through pyproject.toml,
* the working directory is changed during the execution of a test case,
* the test case runs a new Python interpreter with subprocess.run.

When all those conditions are met, the test run completes correctly, but a DateError occurs in coverage when building
the report:

> INTERNALERROR>     raise DataError("Can't combine branch coverage data with statement data")
> 
> INTERNALERROR> coverage.exceptions.DataError: Can't combine branch coverage data with statement data

# How to reproduce the issue

1. Clone the repository.
2. Install the dependencies with `poetry install` or `pip install -r requirements.txt`.
3. Run the tests with `pytest tests/test.py --cov`, it fails.
4. Run the tests with `pytest tests/test.py --cov --cov-branch`, it does not fail.

Of the 4 testcases in test.py, only `test_run_with_cwd` triggers the issue.

This have been reproduced with Python 3.10 to 3.13 under Linux (WSL) and only with 3.13 under Windows.

# Workaround
If enabling branche coverage through `pyproject.toml`, adding `--cov-branch` to the pytest addopts configuration in
`pyproject.toml` will avoid the issue.