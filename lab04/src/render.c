#include <stdio.h>
#include <unistd.h>

#include "../inc/render.h"
#include "../inc/board.h"
#include "../inc/cell.h"

void render_board(cell_entity board[height_y][width_x])
{
  for (int i = 0; i < height_y; i++){
    for (int j = 0; j < width_x; j++){
      switch (board[i][j].cell_type){
        case WALL:
          putchar('#');
          break;
        case DEAD:
          putchar(' ');
          break;
        case ALIVE:
          putchar('O');
          break;  
        default:
          putchar('?');
          break;
      }
    }
    putchar('\n');
  }
  fflush(stdout);
}

void draw_frame(cell_entity board[height_y][width_x])
{
  printf("\033[H");
  render_board(board);
}