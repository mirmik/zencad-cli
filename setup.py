#!/usr/bin/env python3

from wheel.bdist_wheel import bdist_wheel as bdist_wheel_
from setuptools import setup, Extension, Command
from distutils.util import get_platform

import zencad

import glob
import sys
import os

setup(
	name = 'zencad-cli',
	packages = ['zencad-cli'],
	version = '0.1.0',
	license='MIT',
	description = 'CAD system for righteous zen programmers ',
	author = 'Sorokin Nikolay',
	author_email = 'mirmikns@yandex.ru',
	url = 'https://mirmik.github.io/zencad/',
	keywords = ['testing', 'cad'],
	classifiers = [],
	scripts = ["routine/zencad"],

	package_data={},

	#data_files = [
	#	("zencad/examples", [file for file in glob.glob("examples/*.py")]),
	#	*[("zencad/examples/"+d, [file for file in glob.glob("examples/"+d+"/*")]) for d in os.listdir("examples") if os.path.isdir(os.path.join("examples", d)) and d != "__pycache__"]
	#],

	include_package_data=True,
	install_requires=[
		'evalcache==1.8.0',
		'pyservoce==1.9.0',
		'numpy',
		'pillow',
		'inotify',
		'PyQt5',
		'zencad-cli',
	],
)