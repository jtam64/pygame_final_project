import json

class Score:
    def __init__(self):
        '''Initiate score class with scores list to handle highscores. A newest variable to handle the players current score
        '''
        self.scores = {}
        self.highest = {}
        self.newest = {}

        self.reads()
        self.high_score()
        self.get_newest()

    def high_score(self) -> object:
        pass

    def add_score(self, new_score: object):
        '''Add scores object to the scores db

        Args:
            new_score (object): An object to be added to the db with name as key and score as value
        '''
        # set newest score to new_score
        self.newest = new_score
        self.scores["newest"] = new_score
        key, value = list(new_score.keys())[0], list(new_score.values())[0]

        # check if player exists 
        if key in list(self.scores["scores"].keys()):
            # if player exists, check if score is higher
            if self.scores["scores"][key] < value:
                self.scores["scores"].update(new_score)
        else:
            # if player doesnt exist, add player and score to db
            self.scores["scores"].update(new_score)

    def __add__(self, new_score: object):
        '''Dunder method to call the add_score method

        Args:
            new_score (object): Newest score to add to the scores list
        '''
        self.add_score(new_score)
    
    def get_newest(self) -> object:
        '''Sets the newest score attribute to the newest score in JSON file
        '''
        
        self.scores["newest"]
    
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
