[![image](https://img.shields.io/pypi/v/markings.svg)](https://pypi.org/project/markings)
[![Build Status](https://app.travis-ci.com/yeger00/markings.svg?branch=master)](https://app.travis-ci.com/yeger00/markings)

# Markings
`markings` is a library that provides a way to mark your Python module, usually with issues.
Because it is part of the code, it enable you to have an "up to date" list of issues, per a commit, and to be able to view the trends of the issues along the git commits as oppose to using an external [issue tracking system](https://en.wikipedia.org/wiki/Issue_tracking_system).

The library is based on [pytest's markers](https://docs.pytest.org/en/6.2.x/example/markers.html) and especially on `@pytest.mark.xfail`.

# Example
Import the `marker` from the `markings` module.
Decide how you want to mark a fuction and use the decorator to mark the function.
```
from markings import marker

@marker.todo("Receive the name of the user as parameter")
def func():
    print("hello world")
```
In the previous example the `marker` was `todo`, but it can be anything you want:
```
from markings import marker

@marker.anything_you_want("Receive the name of the user as parameter")
def func():
    print("hello world")
```

# Installation
```
pip install markings
```

# Tests
```
./scripts/test.sh
```

# Lint

# How to contribute
