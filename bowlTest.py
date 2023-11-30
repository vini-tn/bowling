import unittest
import bowlGame

class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = bowlGame.BowlingGame()

    def testGutterGame(self):
        for _ in range(0, 20):
            self.game.roll(0)
        assert self.game.score()==0
    def testAllOnes(self):
        self.rollMany(1, 20)
        assert self.game.score()==20
    def testOneSpare(self):
        self.game.roll(5)
        self.game.roll(5)
        self.game.roll(3)
        self.rollMany(0,17)
        assert self.game.score()==16
    def testOneStrike(self):
        self.game.rolls(10)
        self.game.rolls(4)
        self.game.rolls(3)
        self.rollMany(0,16)
        assert  self.game.score()==24
    def testPerfectGame(self):
        self.rollMany(10,12)
        assert self.game.score()==300
    def testOneSpareRM(self):
        self.rollMany(5,21)
        assert self.game.score()==150
    def rollMany(self, pins,rolls):
        for _ in range(rolls):
            self.game.roll(pins)
			
