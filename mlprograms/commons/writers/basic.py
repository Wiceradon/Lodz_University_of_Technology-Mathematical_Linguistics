# This Python file uses the following encoding: utf-8
'''
Created on 17-12-2013

@author: Jakub Jeleński
'''

class SimpleWriter:
    '''
    Writer sending text to standard console output
    '''


    def write(self, data):
        '''
        Print data onto console output
        
        Args:
            data: an object that can be represented as a String (implementing __str__ method)
        '''
        print str(data)