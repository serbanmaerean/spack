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


class PyNestle(PythonPackage):
    """Nested sampling algorithms for evaluating Bayesian evidence."""

    homepage = "http://kbarbary.github.io/nestle/"
    url = "https://pypi.io/packages/source/n/nestle/nestle-0.1.1.tar.gz"

    version('0.1.1', '4875c0f9a0a8e263c1d7f5fa6ce604c5')

    # Required dependencies
    depends_on('py-numpy', type=('build', 'run'))

    # Optional dependencies
    depends_on('py-scipy', type=('build', 'run'))
