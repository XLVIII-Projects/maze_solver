from graphics import Line, Point

class Cell:    
    def __init__(self, _win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None    
        self._y1 = None
        self._y2 = None
        self._win = _win

    def assign_window(self, _win):
        self._win = _win
       
    def __repr__(self):
        return f"Cell({self._x1}, {self._y1}, {self._x2}, {self._y2})"

    def draw(self, _x1, _y1, _x2, _y2):
        if self._win == None:
            return

        self._x1 = _x1
        self._x2 = _x2    
        self._y1 = _y1
        self._y2 = _y2

        if self.has_left_wall:
            line = Line(Point(self._x1,self._y1), Point(self._x1, self._y2))
            self._win.draw_line(line, "black")
        if self.has_right_wall:
            line = Line(Point(self._x2,self._y2), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.has_top_wall:
            line = Line(Point(self._x1,self._y1), Point(self._x2, self._y1))
            self._win.draw_line(line, "black")
        if self.has_bottom_wall:
            line = Line(Point(self._x1,self._y2), Point(self._x2, self._y2))
            self._win.draw_line(line, "black")

    def draw_move(self, to_cell, undo=False):
        fill_color = "grey" if undo else "red"

        point_from = Point(abs(self._x2 - self._x1)//2 + self._x1, 
                           abs(self._y2 - self._y1)//2 + self._y1)
        point_to = Point(abs(to_cell._x2 - to_cell._x1)//2 + to_cell._x1, 
                         abs(to_cell._y2 - to_cell._y1)//2 + to_cell._y1)

        line = Line(point_from, point_to)
        self._win.draw_line(line, fill_color)