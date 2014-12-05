# -*- coding: utf-8 -*-

import subprocess
from setuptools import setup, find_packages, Command
from textile2rst import __version__

version = '.'.join(str(x) for x in __version__)

def read_description():
    with open('README.rst') as fd:
        return fd.read()


class PyTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import sys,subprocess
        errno = subprocess.call([sys.executable, 'runtests.py', 'tests'])
        raise SystemExit(errno)


setup(name='textile2rst',
      version=version,
      description="Small utility to help moving from Jekyll/Octopress textile to Nikola ReStructured Text",
      long_description=read_description(),
      cmdclass = {'test': PyTest},
      classifiers=[
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.2',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Environment :: Console',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Operating System :: OS Independent',
      ],
      keywords='color terminal',
      author='Miguel Ángel García',
      author_email='miguelangel.garcia@gmail.com',
      url='https://github.com/magmax/textile2rst',
      license='MIT',
      packages=find_packages(exclude=['tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
      ],
      )
