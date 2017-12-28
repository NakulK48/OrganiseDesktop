# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import sys
if sys.version_info < (2,):
    sys.exit("Python 1 is not supported...")

with open('README.rst') as f:
    longd = f.read()

setup(
    name='OrganiseDesktop',
    include_package_data=True,
    packages=["os", "getpass", "time","sys","tkinter", "json"],
    data_files=[('OrganiseDesktop', ['OrganiseDesktop/user_agents.txt'])],
    entry_points = {"console_scripts": ['socli = socli.socli:main']},
    install_requires=['BeautifulSoup4','requests','colorama','Py-stackExchange', 'urwid'],
    requires=['os','getpass','time','sys','tkinter'],
    version='1.0',
    url='https://github.com/blavejr/OrganiseDesktop.git',
    keywords="Desktop Organiser",
    license='MIT',
    author='Remigius Kalimba',
    author_email='kalimbatech@gmail.com',
    description='Organise your desktop with one click.',
    long_description="\n\n"+longd
    )
