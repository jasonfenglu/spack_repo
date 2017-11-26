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
#     spack install py-smmap2
#
# You can edit this file again by typing:
#
#     spack edit py-smmap2
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PySmmap2(PythonPackage):
    """A pure python implementation of a sliding window memory map manager."""

    homepage = "https://pypi.python.org/pypi/smmap2"
    url      = "https://github.com/gitpython-developers/smmap/archive/v2.0.3.tar.gz"

    version('2.1.1.dev1', '106c24b362a41b328734897f6d7d2286')
    version('2.1.1.dev0', '8a6d98270d29d042591a2177fe4cac3e')
    version('2.1.0.dev4', '65d22961a462403152faefa7a6450c3a')
    version('2.1.0.dev3', '15978f60b6656392f408eb22e56e527c')
    version('2.1.0.dev2', '6535ce1b2a7f8feb095fe5b7fddbe56a')
    version('2.1.0.dev1', '72d31e7d3a3f805bf5fbd1ec7e2ecc95')
    version('2.1.0.dev0', '55e389f2f54424c6e486f758f439eafb')
    version('2.0.3',      '87427acfb9d65867544d34a12434e502', preferred=True)
    version('2.0.2',      '4d98282008057d333b94849db173cb57')
    version('2.0.1',      '416fccd348725017c03f15dc2b5836f5')

    depends_on('py-setuptools', type=('build'))
