/* -*- C -*- */
// Copyright (C) 2009-2011 Johan Hake
//
// This file is part of DOLFIN.
//
// DOLFIN is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
//
// DOLFIN is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Lesser General Public License for more details.
//
// You should have received a copy of the GNU Lesser General Public License
// along with DOLFIN. If not, see <http://www.gnu.org/licenses/>.
//
// First added:  2009-09-03
// Last changed: 2011-10-09

#ifndef __DOLFIN_DEFINES_H
#define __DOLFIN_DEFINES_H

#include <string>

// Return true if DOLFIN is compiled with OpenMP
bool has_openmp();

// Return true if DOLFIN is compiled with MPI
bool has_mpi();

// Return true if DOLFIN is compiled with SLEPc
bool has_slepc();

// Return true if DOLFIN is compiled with Trilinos
bool has_trilinos();

// Return true if DOLFIN is compiled with Scotch
bool has_scotch();

// Return true if DOLFIN is compiled with CGAL
bool has_cgal();

// Return true if DOLFIN is compiled with Umfpack
bool has_umfpack();

// Return true if DOLFIN is compiled with Cholmod
bool has_cholmod();

// Return true if DOLFIN is compiled with parmetis
bool has_parmetis();

// Return true if DOLFIN is compiled with GMP
bool has_gmp();

// Return true if DOLFIN is compiled with ZLIB
bool has_zlib();

// Return true if a specific linear algebra backend is supported
bool has_linear_algebra_backend(std::string backend);

#endif
