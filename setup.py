#!/usr/bin/env python3

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name = 'pytrends_demo',
    version = '1.0.0',
    description = 'Simple script for loading and displaying Google Trends data',
    author = 'JoshuaBrockschmidt',
    author_email = 'JoshuaBrockschmidt@gmail.com',
    url = 'https://github.com/JoshuaBrockschmidt/pytrends_test',
    scripts = ['scripts/pytrends_demo.py'],
    install_requires = [
        'pytrends>=3',
        'matplotlib>=1'
    ]
)
