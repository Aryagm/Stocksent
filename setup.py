# Always prefer setuptools over distutils
# To use a consistent encoding
from codecs import open
from os import path

from setuptools import setup

# The directory containing this file
HERE = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(HERE, 'README.md')) as f:
    long_description = f.read()

# This call to setup() does all the work
setup(
    name="stocksent",
    version="0.4.4",
    description="A Python library for sentiment analysis of various tickers from the latest news by trusted sources, "
                "and tools to plot results.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://stocksent.readthedocs.io/",
    author="Arya Manjaramkar",
    author_email="aryagm01@email.com",
    license="Mozilla Public License 2.0",
    classifiers=[
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Natural Language :: English",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent"
    ],
    packages=["stocksent"],
    include_package_data=True,
    install_requires=["numpy", "matplotlib",
                      "pandas", "nltk", "wordcloud", "bs4"]
)
