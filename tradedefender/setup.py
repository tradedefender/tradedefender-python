#!/usr/bin/env python3

from setuptools import setup

setup(name='tradedefender',
      version='0.1',
      description='Interface for Trade Defender financial data',
      url='https://tradedefender.com',
      author='CJ Black',
      author_email='cj@tradedefender.com',
      license='MIT',
      packages=['tradedefender'],
      install_requires=['requests'],
      zip_safe=False)
