import pathlib
from setuptools import setup, find_packages

basedir = pathlib.Path(__file__).parent
reqs_file = basedir / 'requirements.txt'
deps = reqs_file.read_text().split('\n')

setup(name='witrn-driver',
      version='0.1.2',
      install_requires=deps,
      packages=find_packages(),
      zip_safe=True,
      platforms='any',
      package_data={
          '': [str(reqs_file)],
      })
