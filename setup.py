import pathlib
from setuptools import setup, find_packages

basedir = pathlib.Path(__file__).parent
reqs_file = basedir / 'requirements.txt'
deps = reqs_file.read_text().split('\n')

setup(name='witrn-driver',
      version='0.1.0',
      description='Driver for reading data from modern WITRN meters',
      author='didim99',
      url = 'https://github.com/didim99/witrn-driver',
      install_requires=deps,
      packages=find_packages(),
      zip_safe=True,
      platforms='any')
