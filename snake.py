import game_functions as gf

class Snake():
    def __init__(self, init_body, init_direction):
        self.body = init_body
        self.direction = init_direction
        self.tail = [(0,0)]

    def take_step(self, board):
        head = self.get_head()
        tail = self.get_tail()
        board.board[tail[1]][tail[0]] = None
        direction = (head[0] + self.direction.value[0], head[1] + self.direction.value[1])
        self.tail  = [self.body[0]]
        self.body = self.body[1:] + [direction]

    def extend_body(self):
        self.body = self.tail + self.body

    def get_direction(self):
        return self.direction

    def set_direction(self, direction):
        self.direction = direction
    
    def get_head(self):
        return self.body[-1]
    
    def get_tail(self):
        return self.body[0]