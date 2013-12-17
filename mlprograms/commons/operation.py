'''
Created on 17-12-2013

@author: Jakub Jeleński
'''

class Operation:
    '''
    Class to neatly perform different kind of operations on 2 values
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.operationMapping = {"+":(lambda x,y: x+y),
                                 "-":(lambda x,y: x-y),
                                 "*":(lambda x,y: x*y),
                                 "/":(lambda x,y: x/y)}
        
    def perform(self, operation, value1, value2):
        '''
        Perform operation.
        
        Args:
            operation: string, operation that should be performed (if possible)
            value1: operand
            value2: operand
        Returns:
            result of operation ( value1 operation value2 )
        Raises:
            TypeError: if value1 or value2 is not a number
            RuntimeError: if operation is not specified in dictionary
        '''
        if operation not in self.operationMapping.keys():
            raise RuntimeError('Operation "%s" is not allowed' % operation)
        
        return self.operationMapping[operation](value1, value2)
        