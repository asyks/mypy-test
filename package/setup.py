from setuptools import setup, find_packages

PKG = 'package'
VERSION = '0.0.1'

setup(
    name=PKG,
    version=VERSION,
    url='https://github.com/asyks/mypy-test',
    author='asyks',
    author_email='aaron@aaronsykes.com',
    description='fake package for testing mypy stub file types.',
    packages=find_packages(),
    package_data={
        PKG: ["py.typed", "*.pyi"]
    },
    include_package_data=True,
)
