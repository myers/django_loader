#!/usr/bin/env python

from distutils.core import setup

setup(name='django_loader',
      version='1.0',
      description='simple module to look in parent dirs of the file that imports this for a django project and loads that project',
      author='Myers Carpenter',
      author_email='myers@maski.org',
      url='https://github.com/myers/django_loader/',
      py_modules=['django_loader'],
     )

