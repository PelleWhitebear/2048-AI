class AIWeights:
    def __init__(self, w_open : float, w_edge : float, w_mono : float, w_merge : float, w_empty : float = 0.0, SnakeMatrix : bool = True):
        self.w_open = w_open
        self.w_edge = w_edge
        self.w_mono = w_mono
        self.w_merge = w_merge
        self.w_empty = w_empty
        self.SnakeMatrix = SnakeMatrix

    def __repr__(self):
        return f"AIWeights(w_open={self.w_open}, w_edge={self.w_edge}, w_mono={self.w_mono}, w_merge={self.w_merge}, w_empty={self.w_empty}, snakeMatrix{self.SnakeMatrix}"
