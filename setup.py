from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='panther_utils',
    url="https://panther.com",
    author="Panther Labs Inc.",
    author_email="support@panther.io",
    version='0.0.1',
    packages=find_packages(),
    python_requires=">=3.9",
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='security detection',
    install_requires=[
        'panther_core>=0.0.6,<0.1.0',
    ],
    classifiers=[
        'Development Status :: 1 - Planning',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Topic :: Security',
        'Typing :: Typed',
        'Programming Language :: Python :: 3',
    ]
)
