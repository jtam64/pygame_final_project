import json

class Score:
    def __init__(self):
        self.scores = []
        self.newest = ""

        self.reads()
    
    def high_score(self):
        pass

    def add_score(self, new_score):
        self.scores.append(new_score)
        self.newest = new_score
    
    def __add__(self, new_score):
        self.add_score(new_score)
    
    def __str__(self):
        return self.newest
    
    def writes(self):
        pass

    def reads(self):
        with open ("scores.json", "r") as file:
            self.scores = json.load(file)