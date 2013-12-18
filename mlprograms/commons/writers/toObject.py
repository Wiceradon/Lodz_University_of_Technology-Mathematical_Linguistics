# This Python file uses the following encoding: utf-8
'''
Created on 17-12-2013

@author: Jakub Jeleński
'''
import basic


class ObjectTextWriter(basic.SimpleWriter):
    '''
    Writer writing to object text state not loosing it (appending to existing text)
    '''


    def __init__(self, writable):
        '''
        Constructor
        
        Args:
            writable: object that implements methods: getText() and setText()
        '''
        self.writable = writable
        
    def write(self, data):
        '''
        Append data to internal text of writable object
        
        Args:
            data: an object that can be represented as a String (implementing __str__ method)
        '''
        currentText = self.writable.getText()+"\n" if len(self.writable.getText()) != 0 else ""
        self.writable.setText(currentText+str(data))