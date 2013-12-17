'''
Created on 17-12-2013

@author: Jakub Jeleński
'''
import mlprograms.commons.writers.basic as basic
import mlprograms.commons.operation as operation

class RpnParser:
    '''
    '''
    
    def __init__(self, writer = basic.SimpleWriter, tokenizedInput):
        '''
        Constructor
        
        Args:
            writer: object that implements method write(data), eg. SimpleWriter, ObjectTextWriter
            tokenizedInput: list of object that represent RPN (numbers and operators)
        '''
        
        self.writer = writer
        self.right = tokenizedInput
        self.left = []
        self.performer = operation.Operation()
        self.currentElem = ''
        
    def parse(self):
        '''
        
        '''
        
        if(len(self.right)==0): return self.left[0]
        self.nextElement()
        return self.parse()
        
    def nextElement(self):
        self.currentElem = self.right.pop(0)
        if self.performer.isAllowed(self.currentElem):
            self.writer.write("Executing operation: "+self.currentElem)
            self.performOperation()
        else:
            self.writer.write("Adding to a stack: "+self.currentElem)
            self.left.append(float(self.currentElem))
            self.writer.write("Current state of a stack: "+str(self.left))
            
    def performOperation(self):
        if len(self.left) > 1:
            v1 = self.left.pop()
            v2 = self.left.pop()
            res = self.performer.perform(self.currentElem, v2, v1)
            self.left.append(res)
            self.writer.write("Adding result to a stack: "+self(res))
            self.writer.write("Current state of a stack: "+str(self.left))