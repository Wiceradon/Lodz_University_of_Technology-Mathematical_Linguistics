# This Python file uses the following encoding: utf-8
'''
Created on 18-12-2013

@author: Jakub Jeleński
'''
import unittest
from mlprograms.rpn.parser import RpnParser


class Test(unittest.TestCase):
    
    def setUp(self):
        self.parser = RpnParser(tokenizedInput=[])


    def testOperationExecution(self):
        self.parser.left = [1]
        self.parser.performOperation()
        self.assertEqual([1], self.parser.left, "[1] != "+str(self.parser.left))
        
        self.parser.left = [1,2]
        self.parser.currentElem = "+"
        self.parser.performOperation()
        self.assertEqual([3], self.parser.left, "[3] != "+str(self.parser.left))
        
        self.parser.left = [1,2,3]
        self.parser.currentElem = "*"
        self.parser.performOperation()
        self.assertEqual([1,6], self.parser.left, "[1,6] != "+str(self.parser.left))
        
    def testNextStep(self):
        self.parser.right = ["1","2","+"]
        self.parser.left= []
        self.parser.nextStep()
        self.assertEqual([1], self.parser.left, "left: [1] != "+str(self.parser.left))
        self.assertEqual(["2","+"], self.parser.right, "right: [2,+] != "+str(self.parser.right))
        
        self.parser.nextStep()
        self.assertEqual([1,2], self.parser.left, "left: [1,2] != "+str(self.parser.left))
        self.assertEqual(["+"], self.parser.right, "right: [+] != "+str(self.parser.right))
        
        self.parser.nextStep()
        self.assertEqual([3], self.parser.left, "left: [3] != "+str(self.parser.left))
        self.assertEqual([], self.parser.right, "right: [] != "+str(self.parser.left))
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()