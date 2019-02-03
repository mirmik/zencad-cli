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
	version = '0.1.1',
	license='MIT',
	description = 'CAD system for righteous zen programmers ',
	author = 'mirmik',
	author_email = 'mirmikns@yandex.ru',
	url = 'https://mirmik.github.io/zencad/',
	keywords = ['testing', 'cad'],
	classifiers = [],
	scripts = ["routine/zencad"],
)
