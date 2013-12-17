'''
Created on 17-12-2013

@author: Jakub Jeleński
'''
import basic


class ObjectTextWriter(basic.SimpleWriter):
    '''
    classdocs
    '''


    def __init__(self, writable):
        '''
        Constructor
        '''
        self.writable = writable
        
    def write(self, data):
        currentText = self.writable.getText()
        self.writable.setText(currentText+"\n"+str(data))