"""
Cerberus - Authentication and authorisation microservice.
"""

import os.path
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))

ABOUT = {}
with open(os.path.join(HERE, 'src', 'cerberusauth', '__version__.py')) as f:
    exec(f.read(), ABOUT)

with open('README.md') as fp:
    README = fp.read()

with open('CHANGES.md') as fp:
    CHANGES = fp.read()

LONG_DESC = """
{}

{}
""".format(README, CHANGES)

with open('LICENSE') as f:
    license = f.read()

REQUIRED = [
    'alembic',
    'bcrypt',
    'nameko',
    'pika',
    'psycopg2-binary',
    'python-slugify',
    'pyyaml',
    'sqlalchemy',
    'sqlalchemy-repr',
    'sqlalchemy-utc',
    'sqlalchemy-utils'
]

setup(
    name=ABOUT['__title__'],
    version=ABOUT['__version__'],
    description=ABOUT['__description__'],
    author=ABOUT['__author__'],
    author_email=ABOUT['__author_email__'],
    url=ABOUT['__url__'],
    license=license,
    long_description=LONG_DESC,
    install_requires=REQUIRED,
    packages=find_packages('src', exclude=('tests', 'docs')),
    package_dir={'': 'src'},
    scripts=[
        'bin/wait-for-it.sh'
    ]
)
