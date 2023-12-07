#REFACTORED: 'Test.py' -> 'bowlTest.py' Changed for clearer understanding what the file is for
#imports unittest from python and 'bowlGame' from 'bowlGame.py'
import unittest
import bowlGame

'''
This file contains 6 test cases of different types of games using the bowlGame.py functions
'''
class TestBowlingGame(unittest.TestCase):

    '''
    Assigns 'self.game' with 'BowlingGame()' class from 'bowlGame' file. This way, each test case starts with a fresh state and doesn't mix with other cases.
    '''
    def setUp(self):
        self.game = bowlGame.BowlingGame()

    '''
    'GutterGame': rolling '0 pins' for 20 rolls (10 Frames total) Breakdown (no spares or stikes detected):
    Frame 1: 0 + 0 = 0
    Frame 2: 0 + 0 = 0
    ...
    Frame 10: 0 + 0 = 0
    Total: 0
    Case passes when score equals '0'
    '''
    def testGutterGame(self):
        #REFACTORED: usage of 'rollMany' as original code contained the same functionality of 'rollMany()'
        self.rollMany(0,20)
        assert self.game.score()==0

    '''
    'AllOnes': rolling '1 pin' for 20 rolls (no fixes required) Breakdown (no spares or stikes detected):
    Frame 1: 1 + 1 = 2
    Frame 2: 1 + 1 = 2
    ...
    Frame 10: 1 + 1 = 2
    Total: (2 * 10) = 20
    Case passes when score equals '20'
    '''
    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score()==20


    '''
    'OneSpare': rolling '5 pins', then '5 pins', then '3 pins', then '0 pins' for 17 turns. Breakdown:
    Frame 1: 5 + 5 + (f2: 3) = 13 (spare bonus)
    Frame 2: 3 + 0 = 3
    Frame 3: 0 + 0 = 0
    ...
    Frame 10: 0 + 0 = 0
    Total: 16
    Case passes when score equals '16'
    '''
    def testOneSpare(self):
        #FIXED: '.rolls' -> '.roll' according to function name in 'bowlGame.py'
        #REFACTORED: Replaced two 'self.game.roll(5)' with 'rollMany(5, 2)' to reduce duplicate lines
        self.rollMany(5,2)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score()==16


    '''
    'OneStrike': rolling '10 pins', then '4 pins', then '3 pins', then '0 pins' for 16 roll. Breakdown:
    Frame 1: 10 + (f2: 4) + (f2: 3) = 17 (strike bonus)
    Frame 2: 4 + 3 = 7
    Frame 3: 0 + 0 = 0
    ...
    Frame 10: 0 + 0 = 0
    Total: 24
    Case passes when score equals '24'
    '''
    def testOneStrike(self):
        #FIXED: '.rolls' -> '.roll' according to function name in 'bowlGame.py' (for all 3 'self.game')
        self.game.roll(10)
        self.game.roll(4)
        self.game.roll(3)
        self.rollMany(0,16)
        assert  self.game.score()==24

    '''
    'PerfectGame': rolling '10 pins' for 12 rolls. Breakdown:
    Frame 1: 10 + (f2: 10) + (f3: 10) = 30 (strike bonus)
    Frame 2: 10 + (f3: 10) + (f4: 10) = 30 (strike bonus)
    ...
    Frame 10: 10 + 10 + 10 = 30 (strike bonus roll)
    Total: 30 * 10 = 300
    Case passes when score equals '300'
    '''
    def testPerfectGame(self):
        self.rollMany(10,12)
        assert self.game.score()==300
    
    '''
    'OneSpareRM': rolling '5 pins' for 21 turns. Breakdown:
    Frame 1: 5 + 5 + (f2: 5) = 15 (spare bonus)
    Frame 2: 5 + 5 + (f3: 5) = 15 (spare bonus)
    ...
    Frame 10: 5 + 5 + 5 = 15 (spare bonus roll)
    Total: 15 * 10 = 150
    Case passes when score equals '150'
    '''
    #REFACTORED: 'testOneSpare' -> 'testOneSpareRM'. Changed because of conflict with earlier 'OneSpare'. RM for only usage of 'rollMany'.
    def testOneSpareRM(self):
        self.rollMany(5,21)
        assert self.game.score()==150

    '''
    'rollMany' consists of using self, pins, and rolls. Creates forloop of 'rolls' where each roll adds 'pins'.
    '''
    def rollMany(self, pins,rolls):
        #REFACTORED: 'i' -> '_'. This changed because 'i' was not used but forloop was needed, hence '_' as a disgarded variable was used.
        for _ in range(rolls):
            #FIXED: '.rolls' -> '.roll' according to function name in 'bowlGame.py'
            self.game.roll(pins)
			
