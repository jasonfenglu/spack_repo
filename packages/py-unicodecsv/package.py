##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/spack/spack
# Please also see the NOTICE and LICENSE files for our notice and the LGPL.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License (as
# published by the Free Software Foundation) version 2.1, February 1999.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the IMPLIED WARRANTY OF
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the terms and
# conditions of the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307 USA
##############################################################################
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install py-unicodecsv
#
# You can edit this file again by typing:
#
#     spack edit py-unicodecsv
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PyUnicodecsv(PythonPackage):
    """The unicodecsv is a drop-in replacement for Python 2.7's csv module which supports unicode strings without a hassle. 
    Supported versions are python 2.6, 2.7, 3.3, 3.4, 3.5, and pypy 2.4.0."""

    homepage = "https://github.com/jdunck/python-unicodecsv"
    url      = "https://github.com/jdunck/python-unicodecsv/archive/0.14.1.tar.gz"
    list_url = "https://github.com/jdunck/python-unicodecsv/archive/"

    version('0.14.1', 'b18cb86aa24cc4e7b862d0470ddc8f39')
    version('0.14.0', 'f70690c47694ce6e717bf1dcdeefc529')
    version('0.13.0', '148fce9e7dfc8443bbfa6574f9b0eeca')
    version('0.12.0', '62b0adddc01113ce17a8fbbe3f52fc4a')
    version('0.11.2', 'dff176abee2b6af851b3798bbfe4ff90')

    # FIXME: Add dependencies if required.
    # depends_on('py-setuptools', type='build')
    # depends_on('py-foo',        type=('build', 'run'))
    depends_on('py-setuptools',   type='build')

