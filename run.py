from easygraphics import easy_run, close_graph, set_fill_color, set_caption, Color, RenderMode, draw_polygon, set_color, clear_device, is_run, init_graph, delay_fps, set_render_mode
from random import randint
from math import floor

max_width = 640
max_height = 480

def make_random_grid(width, height):
    return [[randint(0,1) for i in range(width)] for j in range(height)]

def get_neighbor(grid, x, y):
    #if out of bound return 0
    if x==-1 or y==-1 or y>len(grid)-1 or x>len(grid[0])-1:
       return 0
    return grid[y][x]

def next_gen_cell(grid, x, y):
    neighbors = get_neighbor(grid,x-1,y-1) + get_neighbor(grid,x,y-1) + get_neighbor(grid,x+1,y-1) + get_neighbor(grid,x-1,y) + get_neighbor(grid,x+1,y) + get_neighbor(grid,x-1,y+1) + get_neighbor(grid,x,y+1) + get_neighbor(grid,x+1,y+1)
    
    #life game rules
    if grid[y][x] == 1 and (neighbors == 2 or neighbors == 3):
       return 1
    if grid[y][x] == 0 and  neighbors == 3:
       return 1
    else:
       return 0

def next_gen(grid):
    x_range = range(len(grid[0]))
    y_range = range(len(grid))
    
    new_grid = [[next_gen_cell(grid,i,j) for i in x_range] for j in y_range]
    return new_grid

def draw(grid):
    x_range = range(len(grid[0]))
    y_range = range(len(grid))

    for i in x_range:
       for j in y_range:
          set_fill_color(Color.WHITE if grid[j][i]==0 else Color.BLACK)
          cell_height = floor(max_height/len(grid))
          cell_width = floor(max_width/len(grid[0]))
          x0 = i * cell_width
          x1 = (i+1) * cell_width
          y0 = j * cell_height
          y1 = (j+1) * cell_height
          draw_polygon(  x0,y0,  x0,y1,  x1,y1,  x1,y0)
    return

def mainloop():
    width = floor(max_width / 10)
    height = floor(max_height / 10)
    set_color(Color.BLACK)
    grid = make_random_grid(width, height)
    while is_run():
       delay_fps(10)
       clear_device()
       draw(grid)
       grid = next_gen(grid)

def main():
    init_graph(max_width, max_height)
    set_render_mode(RenderMode.RENDER_MANUAL)
    set_caption("Game of Life")
    mainloop()
    close_graph()

easy_run(main)
