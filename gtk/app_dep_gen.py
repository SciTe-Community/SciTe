#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# app_dep_gen.py - produce a make dependencies file for SciTe
# Copyright 2019-2021 by Neil Hodgson <neilh@scintilla.org>
# Requires Python 3.6 or later
# For copyright information please follow this like:
# https://github.com/SciTe-Community/SciTe/blob/develop/LICENSE
''' GitHub:                           SciTe-Community/SciTe '''

from scripts import Dependencies

import sys

src_root = '../..'
sys.path.append(src_root + '/scintilla')
comment = '# Created by app_dep_gen.py. To recreate, run app_dep_gen.py.\n'

def generate():
	''' This is generate() function '''

	scite_sources = ['../src/*.cxx', '../lua/src/*.c', '../../lexilla/access/*.cxx', '../../scintilla/call/*.cxx']
	scite_includes = ['../../lexilla/include', '../../lexilla/access', '../../scintilla/include', '../src', '../lua/src']

	deps = Dependencies.FindDependencies(['../gtk/*.cxx'] + scite_sources,  ['../gtk'] + scite_includes, '.o', '../gtk/')
	Dependencies.UpdateDependencies('../gtk/deps.mak', deps, comment)

if __name__ == '__main__':
	generate()
