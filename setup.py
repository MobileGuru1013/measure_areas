#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    'numpy',
    'svgwrite',
    'svgpathtools',
    'bottle'
]

setup_requirements = [
    'pytest-runner',
    # TODO(jean): put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest',
    # TODO: put package test requirements here
]

setup(
    name='measure_areas',
    version='0.1.0',
    description="Measure areas of shapes in SVG",
    long_description=readme + '\n\n' + history,
    author="Jean Jordaan",
    author_email='jean@salweensolutions.com',
    url='https://github.com/jean/measure_areas',
    packages=find_packages(include=['measure_areas']),
    entry_points={
        'console_scripts': [
            'measure_areas=measure_areas.cli:main',
            'measure_areas_serve=measure_areas.serve:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='measure_areas',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
