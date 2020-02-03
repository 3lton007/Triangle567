# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right')

    def testEquilateralTriangleA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral')

    def testEquilateralTriangleB(self): 
        self.assertEqual(classifyTriangle(10,10,10),'Equilateral')
    
    def testIsocelesTriangleA(self): 
        self.assertEqual(classifyTriangle(3, 3, 2),'Isosceles')
    

    def testScaleneTriangleA(self): 
        self.assertEqual(classifyTriangle(10, 15, 12),'Scalene')

    def testInvalidInputA(self):
        self.assertEqual(classifyTriangle(-1, -1, -1),'InvalidInput')

    def testInvalidInputC(self):
        self.assertEqual(classifyTriangle("200", "0", "0"),'InvalidInput')

    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(5, 1, 1),'NotATriangle')

    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(1, 5, 1),'NotATriangle')

    

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

