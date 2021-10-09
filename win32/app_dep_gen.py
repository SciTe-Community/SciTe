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
sys.path.append(srcRoot + '/scintilla')
comment = '# Created by app_dep_gen.py. To recreate, run app_dep_gen.py.\n'


def generate():
	''' This is generate() function '''

	scite_sources = ['../src/*.cxx", "../lua/src/*.c", "../../lexilla/access/*.cxx", "../../scintilla/call/*.cxx']
	scite_includes = ["../../lexilla/include", "../../lexilla/access", "../../scintilla/include", "../src", "../lua/src"]

	# Header magically injected into Lua builds on Win32 to make Unicode file names work
	lua_substs = {'LUA_USER_H': 'scite_lua_win.h'}

	# Create the dependencies file for g++
	deps = Dependencies.FindDependencies(['../win32/*.cxx'] + scite_sources,  ['../win32'] + scite_includes, '.o', '../win32/', lua_substs)
	# Add Sc1 as the same as SciTeWin
	deps = Dependencies.InsertSynonym(deps, 'SciTEWin.o', 'Sc1.o')
	Dependencies.UpdateDependencies('../win32/deps.mak', deps, comment)
	# Create the dependencies file for MSVC
	# Change extension from ".o" to ".obj"
	deps = [[Dependencies.PathStem(obj) + '.obj', headers] for obj, headers in deps]
	Dependencies.UpdateDependencies('../win32/nmdeps.mak', deps, comment)


if __name__ == '__main__':
	generate()
