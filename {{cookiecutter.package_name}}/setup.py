#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="{{cookiecutter.package_name}}",
    version="0.0.1",
    description="{{cookiecutter.short_description}}",
    author="{{cookiecutter.full_name}}",
    packages=find_packages(),
    setup_requires=["pytest-runner"],
    tests_require=["pytest"],
)
