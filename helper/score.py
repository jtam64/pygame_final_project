import json

class Score:
    def __init__(self):
        '''Initiate score class with scores list to handle highscores. A newest variable to handle the players current score
        '''
        self.scores = {}

        self.reads()
        self.high_score()
    
    def add_score(self, new_score: int):
        '''Add scores object to the scores db

        Args:
            new_score (int): A value to modify newest score in db
        '''
        # set newest score to new_score and write to db
        self.scores["newest"] = new_score
        self.writes()

    def get_newest(self) -> int:
        '''Get newest score

        Returns:
            _type_: Gets newest value in scores
        '''
        return self.scores["newest"]

    def add_score_to_scores(self, name:str, score:int):
        '''Takes name and score input and creates a new_score value, adds score to the db and checks for highscores

        Args:
            name (str): Player name
            score (int): Score for the player
        '''
        new_score = {name: score}
        # check if player exists 
        if name in list(self.scores["scores"].keys()):
            # if player exists, check if score is higher
            if self.scores["scores"][name] < score:
                self.scores["scores"].update(new_score)
        else:
            # if player doesnt exist, add player and score to db
            self.scores["scores"].update(new_score)

        # check highscores
        self.high_score()

    def high_score(self) -> object:
        '''Gets highscore from score list and sets highscore value

        Returns:
            object: Returns an object with name as key and score as value
        '''
        highest = max(self.scores["scores"], key=self.scores["scores"].get)
        highest = {highest: self.scores["scores"][highest]}
        self.scores["highscore"] = highest
        self.writes()
        return highest

    def __add__(self, new_score: int):
        '''Dunder method to call the add_score method

        Args:
            new_score (int): Newest score to add to the scores list
        '''
        self.add_score(new_score)
    
    def sorter(self) -> list:
        return sorted(self.scores["scores"].items(), key=lambda x:x[1], reverse=True)

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

    def get_score(self, name):
        return [name, self.scores["scores"][name]]