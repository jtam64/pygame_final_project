import json

class Score:
    def __init__(self):
        '''Initiate score class with scores list to handle highscores. A newest variable to handle the players current score
        '''
        self.scores = []
        self.newest = 0
        self.reads()
        self.highest = self.high_score()

    
    def high_score(self) -> int:
        '''Returns the highest value in self.scores

        Returns:
            int: highest integer value in self.scores
        '''
        return max(self.scores)

    def add_score(self, new_score: int):
        '''Addes a new score to self.scores and writes to the JSON file. Sets the newest score to the new score to track player score

        Args:
            new_score (int): A value given from the game to add to the scores
        '''
        self.scores.append(new_score)
        self.newest = new_score
        self.writes()
    
    def __add__(self, new_score: int):
        '''Dunder method to call the add_score method

        Args:
            new_score (int): Newest score to add to the scores list
        '''
        self.add_score(new_score)
    
    def __str__(self) -> str:
        '''Converts the newest score to a string and returns it

        Returns:
            str: The newest score in string form
        '''
        return str(self.newest)
    
    def writes(self):
        '''Writes to the JSON file
        '''
        with open ("helper/scores.json", "w") as file:
            json.dump(self.scores, file)

    def reads(self):
        '''Reads the JSON file and sets self.scores to the values in the file
        '''
        with open ("helper/scores.json", "r") as file:
            self.scores = json.load(file)