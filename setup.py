#!/usr/bin/env python
# encoding: UTF-8

import ast
from setuptools import setup
import os.path

__doc__ = open(
    os.path.join(os.path.dirname(__file__), "README.rst"),
    "r"
).read()

try:
    # For setup.py install
    from tor import __version__ as version
except ImportError:
    # For pip installations
    version = str(ast.literal_eval(
        open(os.path.join(
            os.path.dirname(__file__),
            "tor",
            "__init__.py"),
            "r"
        ).read().split("=")[-1].strip()
    ))

setup(
    name="tower_of_rapunzel",
    version=version,
    description="A text-driven web game.",
    author="D Haynes",
    author_email="tundish@gigeconomy.org.uk",
    url="https://github.com/tundish/tower_of_rapunzel",
    long_description=__doc__,
    classifiers=[
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: GNU Affero General Public License v3"
        " or later (AGPLv3+)"
    ],
    packages=["tor", "tor.test"],
    package_data={
        "tor": [
            "data/*.cfg",
            "dialogue/*/*.rst",
            "static/css/*.css",
            "static/img/*.jpg",
            "static/img/*.png",
            "static/audio/*.mp3",
            "static/fonts/*.woff",
            "static/fonts/*.woff2",
        ]
    },
    install_requires=[
        "aiohttp>=3.6.1",
        "balladeer>=0.14.0",
    ],
    extras_require={
        "dev": [
            "flake8>=3.7.0",
            "wheel>=0.33.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "torgame = tor.main:run",
        ],
    },
    zip_safe=True,
)
