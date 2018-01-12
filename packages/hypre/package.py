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
#     spack install hypre
#
# You can edit this file again by typing:
#
#     spack edit hypre
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
import inspect
from spack import *


class Hypre(MakefilePackage):
    """HYPRE is a library of high performance preconditioners and solvers featuring
    multigrid methods for the solution of large, sparse linear systems of equations
    on massively parallel computers."""

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://www.llnl.gov/casc/hypre/"
    url      = "https://github.com/LLNL/hypre/archive/v2.13.0.tar.gz"

    version('2.13.0', '4b688a5c15b6b5e3de5e045ae081b89b')

    depends_on('mpi')

    @property
    def build_directory(self):
        return join_path(self.stage.source_path, 'src')

    def build(self, spec, prefix):
        with working_dir(self.build_directory):
            inspect.getmodule(self).configure('--prefix={0}'.format(prefix))
            inspect.getmodule(self).make('install')

