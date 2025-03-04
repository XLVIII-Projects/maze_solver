from graphics import Window
from maze import Maze
        
def main():
    num_rows = 24
    num_cols = 32
    margin_x = 20
    margin_y = 20
    cell_size_x = 20
    cell_size_y = 20

    screen_width = num_cols * cell_size_x + (margin_x*2)
    screen_height = num_rows * cell_size_y + (margin_y*2)

    win = Window(screen_width, screen_height)

    maze = Maze(margin_x, margin_y, num_rows, num_cols, cell_size_x, cell_size_y, win)
    
    
    # maze.assign_window(win)

    win.wait_for_close()


if __name__ == "__main__":
    main() 
    
    
    
    # c1 = Cell(win)
    # c1.has_right_wall = False
    # c1.draw(40,40,80,80)
    
    # c2 = Cell(win)
    # c2.has_left_wall = False
    # c2.has_bottom_wall = False
    # c2.draw(80,40,120,80)
    # c1.draw_move(c2, False)
    
    # c3 = Cell(win)
    # c3.has_top_wall = False
    # c3.draw(80,80,120,120)
    # c2.draw_move(c3, True)