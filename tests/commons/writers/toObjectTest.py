# This Python file uses the following encoding: utf-8
'''
Created on 18-12-2013

@author: Jakub Jeleński
'''
import unittest
from mlprograms.commons.writers.toObject import ObjectTextWriter

class WritableMock:
    
    def __init__(self):
        self.textInternal = ""
        
    def setText(self, data):
        self.textInternal = data
        
    def getText(self):
        return self.textInternal

class Test(unittest.TestCase):


    def testWrite(self):
        obj = WritableMock()
        writer = ObjectTextWriter(obj)
        writer.write("AA")
        self.assertEqual("AA", obj.textInternal, "AA != "+obj.textInternal)
        writer.write("BB")
        self.assertEqual("AA\nBB", obj.textInternal, "AA\nBB != "+obj.textInternal)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testWrite']
    unittest.main()