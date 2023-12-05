#REFACTORED: 'Bowling.py' -> 'bowlGame.py' Changed for clearer understanding what the file is for
'''
This file contains how the bowling game is structured and its functions for processing the total score of all the frames.
'''
class BowlingGame:
    #initate array to store pins
    def __init__(self):
        self.rolls=[]

    #add number of pins knocked to rolls array
    def roll(self,pins):
        self.rolls.append(pins)

    '''
    Score: handles cases of strike, spare and frame
    In a forloop of 10 frames:
        if roll matches isStrike condition:
            add to score with strikeScore function
            and go to next roll
        else if rolls matches isSpare condition:
            add to score with spareScore function
            and go to second next roll
        else:
            add to score with frameScore function
            and go to second next roll
    '''
    def score(self):
        #REFACTORED: 'results' -> 'totalScore'. Changed for better understanding of what the function is updating and returning
        totalScore = 0
        rollIndex = 0

        for frameIndex in range(10):
            #FIXED: 'if frameIndex in range(10):' -> 'if self.isStrike(rollIndex):' Changed due to condition being always true. Also to check for strike condition if roll is indeed 10
            if self.isStrike(rollIndex):
                #REFACTORED: 'StrikeScore' -> 'strikeScore' To match the casing of other functions
                totalScore += self.strikeScore(rollIndex)
                rollIndex +=1
            elif self.isSpare(rollIndex):
                totalScore += self.spareScore(rollIndex)
                rollIndex +=2
            else:
                totalScore += self.frameScore(rollIndex)
                #FIXED: Indented inwards as part of else statement
                rollIndex +=2
        #FIXED: Indented outwards as part of function return
        return totalScore

    '''
    Conditions: 
        isStrike: first roll equals 10
        isSpare: first roll and second roll equals  10
    '''
    def isStrike(self, rollIndex):
        return self.rolls[rollIndex] == 10
    def isSpare(self, rollIndex):
        return self.rolls[rollIndex]+ self.rolls[rollIndex+1]==10
    
    '''
    Functions to handle score:
        strikeScore: add 10 + second roll and third roll
        spareScore: add 10 + third roll
        frameScore: add first and second roll 
    '''
    #REFACTORED: 'stickeScore' -> 'strikeScore' For clearer understanding of the function's role
    def strikeScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+1]+ self.rolls[rollIndex+2]

    def spareScore(self,rollIndex):
        return  10+ self.rolls[rollIndex+2]

    def frameScore(self, rollIndex):
        return self.rolls[rollIndex] + self.rolls[rollIndex + 1]
		
