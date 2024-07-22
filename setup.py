"""
File: setup.py
Author: Steven "Kabbe" Karbjinsky
Description: Setup configuration for the Ascendify project.

For more information, see: https://github.com/xKabbe/ascendify
"""
from setuptools import setup, find_packages

setup(
    name='ascendify-api',
    version="0.1.0",
    description='API backend for the Ascendify project, using FastAPI for video and data analysis.',
    author='Steven Karbjinsky',
    author_email='steven.karbjinsky@web.de',
    url='https://github.com/xKabbe/sscendify',
    packages=find_packages(where='api'),
    package_dir={'': 'api'},
    include_package_data=True,
    python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            'ascendify-api=api.main:main',
        ],
    },
)
