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
from spack import *


class PyTqdm(PythonPackage):
    """A Fast, Extensible Progress Meter"""

    homepage = "https://github.com/tqdm/tqdm"
    url      = "https://github.com/tqdm/tqdm/archive/v4.19.5.tar.gz"
    list_url = "https://github.com/tqdm/tqdm/archive/"

    version('develop', git='https://github.com/tqdm/tqdm.git')
    version('4.19.5', '56bc285157a282db64cb5e1a4b3c585c')
    version('4.19.4', '0733c09db729e5e14722a55135790e39')
    version('4.19.3', 'dc0cd71fd954d488fbd46ae6297b47cd')
    version('4.19.2', '5c2551d03dce9399116d978d873012bd')
    version('4.19.1', 'e1bfcf69f7fd9ce3405ff9ca70ae9823')
    version('4.19.0', 'e43cbe3571276ba5ea0756f215a7a268')
    version('4.18.0', '46b954203df2a4c7696a0725cb2379e7')
    version('4.17.1', 'b25964567ca3940d34c163c40def169f')
    version('4.17.0', '3bbcaa5d6599946c90a0b6f158409cab')
    version('4.16.0', '50dd207e8e44ef4c92499ee29b673fcb')

    depends_on('py-setuptools', type='build')
