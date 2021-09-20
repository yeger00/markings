#!/usr/bin/env python
import sys
import os
import pathlib
import pkg_resources
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


here = os.path.abspath(os.path.dirname(__file__))
about = {}
MODULE_NAME="markings"
with open(os.path.join(here, MODULE_NAME, "__version__.py"), "r") as f:
    exec(f.read(), about)

with open("README.md", "r", encoding="utf8") as fh:
    long_description = fh.read()

class PyTest(TestCommand):
    user_options = [("pytest-args=", "a", "Arguments to pass to pytest")]

    def initialize_options(self):
        TestCommand.initialize_options(self)
        self.pytest_args = []

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        errno = pytest.main(self.pytest_args)
        sys.exit(errno)

def parse_requirements_file(file_name):
    with pathlib.Path(os.path.join(here, file_name)).open() as requirements_txt:
        install_requires = [
            str(requirement)
            for requirement
            in pkg_resources.parse_requirements(requirements_txt)
        ]
    return install_requires


setup(
    name=MODULE_NAME,
    version=about["__version__"],
    author=about["__author__"],
    author_email=about["__author_email__"],
    description=about["__description__"],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about["__url__"],
    packages=find_packages(),
    install_requires=parse_requirements_file("requirements.txt"),
    tests_require=parse_requirements_file("requirements-test.txt"),
    extras_require={
        'dev': parse_requirements_file("requirements-dev.txt")
    },
    cmdclass={"test": PyTest},
    data_files=[("", ["requirements.txt", "requirements-test.txt", "requirements-dev.txt"])],
)
