from typing import List

from setuptools import find_packages, setup

REQUIRED_PACKAGES: List[str] = []
DEV_PACKAGES: List[str] = [
    'mypy', 'flake8', 'pytest', 'python-language-server[all]'
]

version = '0.0.1'

setup(
    name='nm_py_scripting',
    version=version,
    install_requires=REQUIRED_PACKAGES,
    packages=find_packages(),
    include_package_data=True,
    description=('Python scripting utils'),
    extras_require={'dev': DEV_PACKAGES},
)

# conda install -c conda-forge jupyter_contrib_nbextensions
