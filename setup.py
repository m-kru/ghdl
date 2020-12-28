# EMACS settings: -*-  tab-width: 2; indent-tabs-mode: t -*-
# vim: tabstop=2:shiftwidth=2:noexpandtab
# kate: tab-width 2; replace-tabs off; indent-width 2;
# =============================================================================
#                ____ _   _ ____  _
#   _ __  _   _ / ___| | | |  _ \| |
#  | '_ \| | | | |  _| |_| | | | | |
#  | |_) | |_| | |_| |  _  | |_| | |___
#  | .__/ \__, |\____|_| |_|____/|_____|
#  |_|    |___/
# =============================================================================
# Authors:            Tristan Gingold
#                     Patrick Lehmann
#
# Package installer:  Python binding for GHDL and high-level APIs.
#
# License:
# ============================================================================
# Copyright (C) 2019-2020 Tristan Gingold
#
#	GHDL is free software; you can redistribute it and/or modify it under
#	the terms of the GNU General Public License as published by the Free
#	Software Foundation; either version 2, or (at your option) any later
#	version.
#
#	GHDL is distributed in the hope that it will be useful, but WITHOUT ANY
#	WARRANTY; without even the implied warranty of MERCHANTABILITY or
#	FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
#	for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with GHDL; see the file COPYING.  If not, write to the Free
#	Software Foundation, 59 Temple Place - Suite 330, Boston, MA
#	02111-1307, USA.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ============================================================================
#
import setuptools
from re import compile as re_compile

gitHubNamespace = "ghdl"
projectName = "ghdl"
packageName = "pyGHDL"

# read (local) README for upload to PyPI
with open("README.md", "r") as file:
	long_description = file.read()

# Read requirements file and add them to package dependency list
requirements = []
with open("requirements.txt") as file:
	for line in file.readlines():
		requirements.append(line)

def get_version():
	# Try from version.py.  Reads it to avoid loading the shared library.
	pattern = re_compile('^__version__ = "(.*)"\n')
	try:
		line = open("pyGHDL/libghdl/version.py").read()
		match = pattern.match(line)
		if match:
			return match.group(1)
	except:
		pass

	raise Exception("Cannot find version")

# Derive URLs
sourceCodeURL =     "https://github.com/{namespace}/{projectName}".format(namespace=gitHubNamespace, projectName=projectName)
documentationURL =  "https://{namespace}.github.io/{projectName}/using/py/index.html".format(namespace=gitHubNamespace, projectName=projectName)

# Assemble all package information
setuptools.setup(
	name=packageName,
	version=get_version(),

	author="Tristan Gingold",
	author_email="tgingold@free.fr",

	description="Python binding for GHDL and high-level APIs (incl. LSP).",
	long_description=long_description,
	long_description_content_type="text/markdown",

	url=sourceCodeURL,
	project_urls={
		'Documentation': documentationURL,
		'Source Code':   sourceCodeURL,
		'Issue Tracker': sourceCodeURL + "/issues"
	},

	packages=setuptools.find_packages(),
	entry_points={
		'console_scripts': [
			"ghdl-ls = pyGHDL.cli.lsp:main"
		]
	},
	classifiers=[
		"License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
		"Operating System :: MacOS",
		"Operating System :: Microsoft :: Windows :: Windows 10",
		"Operating System :: POSIX :: Linux",
		"Programming Language :: Python :: 3 :: Only",
		"Programming Language :: Python :: 3.8",
		"Programming Language :: Python :: 3.9",
		"Development Status :: 4 - Beta",
#		"Development Status :: 5 - Production/Stable",
		"Intended Audience :: Developers",
		"Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
		"Topic :: Software Development :: Code Generators",
		"Topic :: Software Development :: Compilers",
		"Topic :: Software Development :: Testing",
		"Topic :: Utilities",
	],
	keywords="Python3 VHDL Parser Compiler Simulator GHDL",

	python_requires='>=3.8',
	install_requires=requirements,
)
