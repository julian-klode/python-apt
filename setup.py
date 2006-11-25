#!/usr/bin/env python

from distutils.core import setup
import glob, os, commands, sys

setup(
    name = 'python-aptsources',
    version = '0.0.1',
    description = 'Abstratcion of the sources.list',
    packages = ['AptSources'],
    data_files = [('share/python-aptsources/templates',
                  glob.glob('build/templates/*.info'))],
    license = 'GNU GPL',
    platforms = 'posix',
    cmdclass = { "build" : build_plus,
                 "build_l10n" :  build_l10n }
)
