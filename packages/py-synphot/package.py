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
#     spack install py-synphot-refactor-git
#
# You can edit this file again by typing:
#
#     spack edit py-synphot-refactor-git
#
# See the Spack documentation for more information on packaging.
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
from spack import *


class PySynphot(PythonPackage):
    """
    synphot simulates photometric data and spectra, observed or otherwise. You can incorporate your own filters, spectra, and data. You can also use a pre-defined standard star (Vega), bandpass, or extinction law. Furthermore, it allows you to:

    Construct complicated composite spectra using different models.
    Simulate observations.
    Compute photometric properties such as count rate, effective wavelength, and effective stimulus.
    Manipulate a spectrum; e.g., applying redshift or normalize it to a given flux value in a given bandpass.
    Sample a spectrum at given wavelengths.
    Plot a quick-view of a spectrum.
    Perform repetitive operations such as simulating the observations of multiple type of sources through multiple bandpasses.
    """

    # FIXME: Add a proper url for your package's homepage here.
    homepage = "http://synphot.readthedocs.io/en/latest/index.html#"
    url      = "https://github.com/spacetelescope/synphot_refactor.git"

    version('develope', git='https://github.com/spacetelescope/synphot_refactor.git')

    depends_on('py-numpy@1.9:')
    depends_on('py-astropy@1.3:')
    depends_on('py-scipy@0.14:')

    depends_on('py-matplotlib') # could be optional in the futrue.

