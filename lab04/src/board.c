#include "../inc/board.h"
#include "../inc/cell.h"

cell_entity main_board[height_y][width_x] = { 0 };
cell_entity buffer_board[height_y][width_x] = { 0 };

void init_board() 
{
  for (int i = 0; i < height_y; i++) {
    for (int j = 0; j < width_x; j++) {
      if (i == 0 || i == height_y - 1 || j == 0 || j == width_x - 1){
        main_board[i][j] = (cell_entity){WALL, j, i};
        buffer_board[i][j] = (cell_entity){WALL, j, i};
      }
      else {
        main_board[i][j] = (cell_entity){DEAD, j, i};
        buffer_board[i][j] = (cell_entity){DEAD, j, i};
      }

    }
  }
}
