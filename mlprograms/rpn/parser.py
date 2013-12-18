# This Python file uses the following encoding: utf-8
'''
Created on 17-12-2013

@author: Jakub Jeleński
'''
import mlprograms.commons.writers.basic as basic
import mlprograms.commons.operation as operation

class RpnParser:
    '''
    Class to parse RPN (Reverse Polish Notation) - execute RPN sequence and produce result
    
    Examples:
        text = [6, 4, +, 2, /]
        text2 = [2, 1, -, 3, *, 1, +]
        text3 = [3, 9, 3, 7, 2, 3, +, -, *, /, +]
        RpnParser(text).parse() => 5
        RpnParser(text2).parse() => 4
        RpnParser(text3).parse() => 4.5
    '''
    
    def __init__(self, tokenizedInput, writer = basic.SimpleWriter()):
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
        self.nextStep()
        return self.parse()
        
    def nextStep(self):
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
            self.writer.write("Adding result to a stack: "+str(res))
            self.writer.write("Current state of a stack: "+str(self.left))