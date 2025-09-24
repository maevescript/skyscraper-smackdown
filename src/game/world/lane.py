class Lane:
    def __init__(self, index, x_start, width):
        self.index = index
        self.x_start = x_start
        self.x_center = x_start + width // 2
        self.width = width