'''
Created on 17-12-2013

@author: Jakub Jeleński
'''

class Operation(object):
    '''
    classdocs
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
        '''
        if operation not in self.operationMapping.keys():
            raise RuntimeError('Operation "%s" is not allowed' % operation)
        
        return self.operationMapping[operation](value1, value2)
        