class Rectangle:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    
    def height(self):
        return self.y2 - self.y1

    def width(self):
        return self.x2 - self.x1  


def is_intersection(R1, R2):
    return R1.x1 < R2.x2 and R1.x2 > R2.x1 and R1.y1 < R2.y2 and R1.y2 > R2.y1

def get_intersection(R1, R2):
    return Rectangle(max(R1.x1, R2.x1), max(R1.y1, R2.y1), min(R1.x2, R2.x2), min(R1.y2, R2.y2,))
