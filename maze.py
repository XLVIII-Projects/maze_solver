from cell import Cell
from graphics import Window
from graphics import Line, Point
import time
import random

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, _win=None, seed=None):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        if seed != None:
            random.seed(seed)

        self.previous_cell = None 
        self._win = _win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            column = []
            for j in range(self.num_rows):
                column.append(Cell(self._win))
            self._cells.append(column)

        self._break_walls_r(0, 0)
        self._reset_cells_visited()
        self._break_entrance_and_exit()

    def _draw_cell(self, i, j):
        if self._win == None:
            return
        # set maze coordinates
        cell_x1 = self.x1 + self.cell_size_x * i
        cell_y1 = self.y1 + self.cell_size_y * j
        cell_x2 = cell_x1 + self.cell_size_x
        cell_y2 = cell_y1 + self.cell_size_y

        # draw cell and move line
        self._cells[i][j].draw(cell_x1, cell_y1, cell_x2, cell_y2)

        self._animate()

    def _break_entrance_and_exit(self):
        # redraw cells
        self._cells[0][0].has_top_wall = False
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False

        temp_previous = self.previous_cell
        self.previous_cell = None
        self._draw_cell(0, 0) 
        self._draw_cell(self.num_cols -1, self.num_rows -1)
        self.previous_cell = temp_previous

        if self._win == None:
            return
        
        # replace old entrance and exit line with white lines
        line_entrance = Line(Point(self.x1, self.y1), 
                             Point(self.x1 + self.cell_size_x, self.y1))
        
        line_exit =     Line(Point(self.x1 + self.cell_size_x * (self.num_cols-1), 
                                   self.y1 + self.cell_size_y * self.num_rows), 
                             Point(self.x1 + self.cell_size_x * self.num_cols, 
                                   self.y1 + self.cell_size_y * self.num_rows))
        
        self._win.draw_line(line_entrance, "white")
        self._win.draw_line(line_exit, "white")

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            adjacent_cells = []

            if i > 0 and self._cells[i-1][j].visited == False:
                adjacent_cells.append("left")
            if i < (self.num_cols - 1) and self._cells[i+1][j].visited == False:
                adjacent_cells.append("right")
            if j > 0 and self._cells[i][j-1].visited == False:
                adjacent_cells.append("top")
            if j < (self.num_rows - 1) and self._cells[i][j+1].visited == False:
                adjacent_cells.append("bottom")

            if not adjacent_cells:
                self._draw_cell(i,j)
                return 
            
            adjacent_cell = random.choice(adjacent_cells)
            if adjacent_cell == "left":
                self._cells[i][j].has_left_wall = False
                self._cells[i-1][j].has_right_wall = False
                self._break_walls_r(i-1,j)
            if adjacent_cell == "right":
                self._cells[i][j].has_right_wall = False
                self._cells[i+1][j].has_left_wall = False
                self._break_walls_r(i+1,j)
            if adjacent_cell == "top":
                self._cells[i][j].has_top_wall = False
                self._cells[i][j-1].has_bottom_wall = False
                self._break_walls_r(i,j-1)
            if adjacent_cell == "bottom":
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j+1].has_top_wall = False
                self._break_walls_r(i,j+1)

    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False

    def solve(self, i, j):
        self._solve_r(i, j)

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if self._cells[i][j] == self._cells[self.num_cols-1][self.num_rows-1]:
            return True
        
        if i > 0 and self._cells[i-1][j].visited == False and self._cells[i][j].has_left_wall == False:
            self._cells[i][j].draw_move(self._cells[i-1][j], False)
            recurse = self._solve_r(i-1, j)
            if recurse is True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i-1][j], True)

        if i < (self.num_cols - 1) and self._cells[i+1][j].visited == False and self._cells[i][j].has_right_wall == False:
            self._cells[i][j].draw_move(self._cells[i+1][j], False)
            recurse = self._solve_r(i+1, j)
            if recurse is True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i+1][j], True)

        if j > 0 and self._cells[i][j-1].visited == False and self._cells[i][j].has_top_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j-1], False)
            recurse = self._solve_r(i, j-1)
            if recurse is True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j-1], True)

        if j < (self.num_rows - 1) and self._cells[i][j+1].visited == False and self._cells[i][j].has_bottom_wall == False:
            self._cells[i][j].draw_move(self._cells[i][j+1], False)
            recurse = self._solve_r(i, j+1)
            if recurse is True:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j+1], True)

        else:
            return False

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        time.sleep(0.05)


        