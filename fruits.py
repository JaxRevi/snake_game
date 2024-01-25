
class Fruits():
    def __init__(self, score) -> None:
        self.fruit_count = 1
        self.fruit_threshold = 10
        self.score = score

    def get_fruit_count(self):
        return self.fruit_count
    
    def passed_threshold(self):
        return self.score.score > self.fruit_threshold
    
    def update_threshold(self):
        self.fruit_threshold += self.fruit_threshold
        self.fruit_count += 1