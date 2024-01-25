

class Bombs():
    def __init__(self, score) -> None:
        self.bomb_count = 1
        self.score = score
        self.bomb_threshold = 10

    def get_bomb_count(self):
        return self.bomb_count
    
    def passed_threshold(self):
        return self.score.score > self.bomb_threshold 
    
    def update_threshold(self):
        self.bomb_threshold += self.bomb_threshold
        self.bomb_count += 1