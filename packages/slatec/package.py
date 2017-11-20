##############################################################################
# Copyright (c) 2013-2017, Lawrence Livermore National Security, LLC.
# Produced at the Lawrence Livermore National Laboratory.
#
# This file is part of Spack.
# Created by Todd Gamblin, tgamblin@llnl.gov, All rights reserved.
# LLNL-CODE-647188
#
# For details, see https://github.com/llnl/spack
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
#     spack install slatec
#
# You can edit this file again by typing:
#
#     spack edit slatec
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
import os
import glob

from spack import *
from spack.stage import Stage
from spack.util.executable import Executable

class Slatec(Package):
    """FIXME: Put a proper description of your package here."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.netlib.org/slatec/"
    url      = "http://www.netlib.org/slatec/slatec_src.tgz"

    version('4.1','f7188cf8c3cc39a65600aabca09490ce')

    #patch('http://www.netlib.org/slatec/slatec4linux.tgz',
    patch('slatec4linux.patch', working_dir='../')

    depends_on('lapack')

    # FIXME: Add dependencies if required.
    # depends_on('foo')

    # def patch(self):
    #     print 'Patching.....'

    #     url = 'http://www.netlib.org/slatec/slatec4linux.tgz'

    #     patch_path = self.stage.path+'/slatec4linux'
    #     with Stage(url, path=patch_path, keep=True) as stage:
    #         stage.fetch()
    #         # stage.expand_archive()

    #     print 'HERE'

    def default_flag_handler(self, env, flag_val):
        flags = flag_val[1]
        if '%intel' in self.spec:
            flags.append('-limf')
            flags.append('-lifcore')
        elif '%clang' in self.spec:
            flags.append('-fPIC')

        return flags

    def install(self, spec, prefix):
        with working_dir(self.stage.path):
            make('all')
            install('libslatec.so', prefix)
            install('libstatic_slatec.a', prefix)
