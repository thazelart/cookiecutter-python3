#!/usr/bin/env python3
from {{cookiecutter.package_name}}.packageutils import simple_example


def test_inc_zero():
    assert simple_example.inc(0) == 1


def test_inc_positive():
    assert simple_example.inc(3) == 4


def test_inc_negative():
    assert simple_example.inc(-2) == -1
