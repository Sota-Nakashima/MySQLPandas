# -*- coding: utf-8 -*-

from setuptools import setup
from codecs import open
from os import path
import re

package_name = "MySQLPandas"

root_dir = path.abspath(path.dirname(__file__))

def _requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'requirements.txt')).readlines()]


def _test_requirements():
    return [name.rstrip() for name in open(path.join(root_dir, 'test-requirements.txt')).readlines()]

with open(path.join(root_dir, package_name, '__init__.py')) as f:
    init_text = f.read()
    version = re.search(r'__version__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    license = re.search(r'__license__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author = re.search(r'__author__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    author_email = re.search(r'__author_email__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)
    url = re.search(r'__url__\s*=\s*[\'\"](.+?)[\'\"]', init_text).group(1)

assert version
assert license
assert author
assert author_email
assert url

with open('README.md', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name=package_name,
    packages=[package_name,f'{package_name}/lib'],

    version=version,

    license=license,

    install_requires=_requirements(),
    #tests_require=_test_requirements(),

    author=author,
    author_email=author_email,

    url=url,

    description='MySQLPandas: simple connector between MySQL(MariaDB) and Pandas',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords='Python, Pandas, Database',

    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Database',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
