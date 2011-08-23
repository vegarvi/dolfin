"""Unit tests for the fem interface"""

# Copyright (C) 2009 Garth N. Wells
#
# This file is part of DOLFIN.
#
# DOLFIN is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# DOLFIN is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with DOLFIN. If not, see <http://www.gnu.org/licenses/>.
#
# First added:  2009-07-28
# Last changed: 2009-07-28

import unittest
import numpy
from dolfin import *

class FiniteElementTest(unittest.TestCase):

    def setUp(self):
        self.mesh = UnitSquare(4, 4)
        self.V = FunctionSpace(self.mesh, "CG", 1)
        self.Q = VectorFunctionSpace(self.mesh, "CG", 1)
        self.W = self.V * self.Q

    def test_evaluate_dofs(self):
        e = Expression("x[0]+x[1]")
        e2 = Expression(("x[0]+x[1]", "x[0]+x[1]"))

        coords = numpy.zeros((3, 2), dtype="d")
        coord = numpy.zeros(2, dtype="d")
        values0 = numpy.zeros(3, dtype="d")
        values1 = numpy.zeros(3, dtype="d")
        values2 = numpy.zeros(3, dtype="d")
        values3 = numpy.zeros(3, dtype="d")
        values4 = numpy.zeros(6, dtype="d")
        for cell in cells(self.mesh):
            self.V.dofmap().tabulate_coordinates(cell, coords)
            for i in xrange(coords.shape[0]):
                coord[:] = coords[i,:]
                values0[i] = e(*coord)
            self.W.sub(0).element().evaluate_dofs(values1, e, cell)
            L = self.W.sub(1)
            L.sub(0).element().evaluate_dofs(values2, e, cell)
            L.sub(1).element().evaluate_dofs(values3, e, cell)
            L.element().evaluate_dofs(values4, e2, cell)

            for i in range(3):
                self.assertAlmostEqual(values0[i], values1[i])
                self.assertAlmostEqual(values0[i], values2[i])
                self.assertAlmostEqual(values0[i], values3[i])
                self.assertAlmostEqual(values4[:3][i], values0[i])
                self.assertAlmostEqual(values4[3:][i], values0[i])

class DofMapTest(unittest.TestCase):

    def setUp(self):
        self.mesh = UnitSquare(4, 4)
        self.V = FunctionSpace(self.mesh, "CG", 1)
        self.Q = VectorFunctionSpace(self.mesh, "CG", 1)
        self.W = self.V*self.Q

    def test_tabulate_coord(self):

        coord0 = numpy.zeros((3,2), dtype="d")
        coord1 = numpy.zeros((3,2), dtype="d")
        coord2 = numpy.zeros((3,2), dtype="d")
        coord3 = numpy.zeros((3,2), dtype="d")
        coord4 = numpy.zeros((6,2), dtype="d")

        for cell in cells(self.mesh):
            self.V.dofmap().tabulate_coordinates(cell, coord0)
            self.W.sub(0).dofmap().tabulate_coordinates(cell, coord1)
            L = self.W.sub(1)
            L.sub(0).dofmap().tabulate_coordinates(cell, coord2)
            L.sub(1).dofmap().tabulate_coordinates(cell, coord3)
            L.dofmap().tabulate_coordinates(cell, coord4)

            self.assertTrue((coord0 == coord1).all())
            self.assertTrue((coord0 == coord2).all())
            self.assertTrue((coord0 == coord3).all())
            self.assertTrue((coord4[:3] == coord0).all())
            self.assertTrue((coord4[3:] == coord0).all())

    def test_tabulate_dofs(self):

        dofs0 = numpy.zeros(3, dtype="I")
        dofs1 = numpy.zeros(3, dtype="I")
        dofs2 = numpy.zeros(3, dtype="I")
        dofs3 = numpy.zeros(6, dtype="I")

        for i, cell in enumerate(cells(self.mesh)):

            self.W.sub(0).dofmap().tabulate_dofs(dofs0, cell)

            L = self.W.sub(1)
            L.sub(0).dofmap().tabulate_dofs(dofs1, cell)
            L.sub(1).dofmap().tabulate_dofs(dofs2, cell)
            L.dofmap().tabulate_dofs(dofs3, cell)

            self.assertTrue(numpy.array_equal(dofs0, \
                                self.W.sub(0).dofmap().cell_dofs(i)))
            self.assertTrue(numpy.array_equal(dofs1,
                                L.sub(0).dofmap().cell_dofs(i)))
            self.assertTrue(numpy.array_equal(dofs2,
                                L.sub(1).dofmap().cell_dofs(i)))
            self.assertTrue(numpy.array_equal(dofs3,
                                L.dofmap().cell_dofs(i)))

            self.assertEqual(len(numpy.intersect1d(dofs0, dofs1)), 0)
            self.assertEqual(len(numpy.intersect1d(dofs0, dofs2)), 0)
            self.assertEqual(len(numpy.intersect1d(dofs1, dofs2)), 0)
            self.assertTrue(numpy.array_equal(numpy.append(dofs1, dofs2), dofs3))

if __name__ == "__main__":
    print ""
    print "Testing PyDOLFIN FiniteElement operations"
    print "------------------------------------------------"
    unittest.main()