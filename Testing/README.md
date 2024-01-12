## unittest

| Commands | Action |
|------|------|
| python -m unittest test.py | Run `test.py`
| python -m unittest -v test.py| `-v` flag for verbose mode
| python -m unittest discover |  search the current directory for any files named `test*.py`
| python -m unittest discover -s tests | `-s` flag to specify directory |
| python -m unittest discover -s tests -t src | `-t` flag to specify the directory if tests in sub directory |


## pytest
Testing framework for python

### Features
* auto discovery of tests
  > identifies tests based on name
* rich assertion introspection
  > provides easy to read reports in case of failure
* supports parameterized and fixture-based testing
  > easily run test with multiple arguments


`pytest tests/test_my_functions.py`