from game_enums import *

class Score():
    def __init__(self) -> None:
        self.score = 0

    def add_score(self, Fruit):
        self.score += Fruit.value