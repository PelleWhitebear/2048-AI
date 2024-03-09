class AIWeights:
    def __init__(self, w_open=12, w_edge=5, w_mono=-2, w_merge=4):
        self.w_open = w_open
        self.w_edge = w_edge
        self.w_mono = w_mono
        self.w_merge = w_merge

    def __repr__(self):
        return f"AIWeights(w_open={self.w_open}, w_edge={self.w_edge}, w_mono={self.w_mono}, w_merge={self.w_merge})"
