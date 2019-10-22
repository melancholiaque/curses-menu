from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand
import sys
import re
import io


setup(
    name='curses-menu',
    url='http://github.com/pmbarrett314/curses-menu',
    license='MIT',
    author='Paul Barrett',
    author_email='pmbarrett314@gmail.com',
    description='A simple console menu system using curses',
    packages=find_packages(),
)
