from easygraphics import *
from random import randint
from math import floor

max_width = 640
max_height = 480

def make_random_grid(width, height):
    return [[randint(0,1) for i in range(width)] for j in range(height)]

def get_grid(grid,x,y):
    #if out of bound return 0
    if x==-1 or y==-1 or y>len(grid)-1 or x>len(grid[0])-1:
       return 0
    return grid[y][x]

def next_gen_cell(grid,x,y):
    neighbors = get_grid(grid,x-1,y-1) + get_grid(grid,x,y-1) + get_grid(grid,x+1,y-1) + get_grid(grid,x-1,y) + get_grid(grid,x+1,y) + get_grid(grid,x-1,y+1) + get_grid(grid,x,y+1) + get_grid(grid,x+1,y+1)
    
    #life game rules
    if grid[y][x] == 1 and (neighbors == 2 or neighbors == 3):
       return 1
    if grid[y][x] == 0 and  neighbors == 3:
       return 1
    else:
       return 0

def next_gen(grid):
    y_size = len(grid)
    x_size = len(grid[0])
    
    new_grid = [[next_gen_cell(grid,i,j) for i in range(x_size)] for j in range(y_size)]
    return new_grid

def draw(grid):
    y_size = len(grid)
    x_size = len(grid[0])
    for i in range(x_size):
       for j in range(y_size):
          set_fill_color(Color.WHITE if grid[j][i]==0 else Color.BLACK)
          cell_height = floor(max_height/y_size)
          cell_width = floor(max_width/x_size)
          x0 = i * cell_width
          x1 = (i+1) * cell_width
          y0 = j * cell_height
          y1 = (j+1) * cell_height
          draw_polygon(  x0,y0,  x0,y1,  x1,y1,  x1,y0)
    return

def mainloop():
    width = 64
    height = 48
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
    mainloop()
    close_graph()

easy_run(main)
