# This Python file uses the following encoding: utf-8
'''
Created on 18-12-2013

@author: Jakub Jeleński
'''
import unittest
from mlprograms.commons.operation import Operation


class Test(unittest.TestCase):
    
    def setUp(self):
        self.op = Operation()

    def testAdd(self):
        self.assertEqual(2.0, self.op.perform("+",1.0,1.0), "2.0 != 1.0+1.0")
        self.assertEqual(6.0, self.op.perform("+",5.0,1.0), "6.0 != 5.0+1.0")
        self.assertEqual(2.1, self.op.perform("+",1.1,1.0), "2.1 != 1.1+1.0")

    def testSub(self):
        self.assertEqual(1.0-1.0, self.op.perform("-",1.0,1.0), "0.0 != 1.0-1.0")
        self.assertEqual(1.0-5.0, self.op.perform("-",1.0,5.0), "-4.0 != 1.0-5.0")
        self.assertEqual(1.1-1.0, self.op.perform("-",1.1,1.0), "0.1 != 1.1-1.0")

    def testMul(self):
        self.assertEqual(1.0, self.op.perform("*",1.0,1.0), "1.0 != 1.0*1.0")
        self.assertEqual(6.0, self.op.perform("*",3.0,2.0), "6.0 != 3.0*2.0")
        self.assertEqual(-2.53, self.op.perform("*",1.1,-2.3), "-2.53 != 1.1*-2.3")

    def testDiv(self):
        self.assertEqual(1.0, self.op.perform("/",1.0,1.0), "1.0 != 1.0/1.0")
        self.assertEqual(2.5, self.op.perform("/",5.0,2.0), "2.5 != 5.0/2.0")
        self.assertEqual(0.55, self.op.perform("/",1.1,2.0), "0.55 != 1.1/2.0")

    def testAllowed(self):
        self.assertEqual(True, self.op.isAllowed("*"), "* should be allowed")
        self.assertNotEqual(True, self.op.isAllowed(""), "Empty operator shouldn't be allowed")
        self.assertNotEqual(True, self.op.isAllowed(")"), ") operator shouldn't be allowed")
        self.assertNotEqual(True, self.op.isAllowed(None), "None operator shouldn't be allowed")
        self.assertNotEqual(True, self.op.isAllowed(1), "Type int as operator shouldn't be allowed")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAdd']
    unittest.main()