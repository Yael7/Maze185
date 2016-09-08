
import unittest
from Maze import *

class testMaze (unittest.TestCase) :
    def setUp (self) :
        # this checks for a Maze class
        self.m=Maze()

    def testScreenExists (self) :
        assert type (self.m.s) == turtle._Screen
        
    def testTurtleExists(self) :
        assert type (self.m.t) == turtle._Turtle

if __name__=="__main__":
    unittest.main(exit=False) 
