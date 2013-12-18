# This Python file uses the following encoding: utf-8
'''
Created on 18-12-2013

@author: Jakub Jeleński
'''
import mlprograms.rpn.parser as ps

if __name__ == '__main__':
    print "*"*5 + " Welcome to CLI for RPN parser software " + "*"*5
    print "*"*5 + " Enter RPN sequence (separated by ' ') " + "*"*5
    print "*"*5 + " Empty sequence will finish program " + "*"*5
    
    string = raw_input()
    while(len(string) != 0):
        parser = ps.RpnParser(string.strip().split())
        print "Result of a given RPN (%s) is %f" % (string, parser.parse())
        print "#"*20
        print "*"*5 + " Enter RPN sequence (separated by ' ') " + "*"*5
        print "*"*5 + " Empty sequence will finish program " + "*"*5
        string = raw_input()
    print "End of the World!"