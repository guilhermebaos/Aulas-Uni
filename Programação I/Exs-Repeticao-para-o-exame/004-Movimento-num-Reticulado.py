class Grid:
    def __init__(self, max_x, max_y, x, y):
        self.max_x = max_x
        self.max_y = max_y
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def up(self):
        new_y = self.y + 1
        if new_y > self.max_y:
            raise OverflowError('too far up')
        self.y = new_y

    def down(self):
        new_y = self.y - 1
        if new_y < 0:
            raise OverflowError('too far down')
        self.y = new_y

    def right(self):
        new_x = self.x + 1
        if new_x > self.max_x:
            raise OverflowError('too far right')
        self.x = new_x

    def left(self):
        new_x = self.x - 1
        if new_x < 0:
            raise OverflowError('too far left')
        self.x = new_x


g = Grid(3, 2, 1, 1)
print(g)
g.up()
print(g)
g.left()
print(g)
g.up()
