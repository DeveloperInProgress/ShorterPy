from setuptools import setup, find_packages

setup(
    name='shorter-py',
    version='0.1.0',
    packages=find_packages(),
    package_dir={'shorter-py': 'shorterpy'},
    include_package_data=True,
)