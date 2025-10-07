#include "../inc/cell.h"
#include "../inc/board.h"
#include "../inc/rules.h"
#include <string.h>


int check_cell_neighbors(cell_entity *cell)
{
  int alive_neghbors = 0;
  int x = cell->pos_x;
  int y = cell->pos_y;

  // Check all 8 neighbors
  for (int i = -1; i <= 1; i++){
    for (int j = -1; j <= 1; j++){

      if (i == 0 && j == 0)
        continue;

      if ( main_board[y + i][x + j].cell_type == ALIVE) {
        alive_neghbors++;
      }

    }
  }  

  return alive_neghbors;
}

void change_cell_state(cell_entity *cell, int alive_neghbors)
{
  if ((alive_neghbors < 2 || alive_neghbors > 3) && cell->cell_type != DEAD) {
    cell_die(&(buffer_board[cell->pos_y][cell->pos_x]));
  } else if ((alive_neghbors == 3) && cell->cell_type != ALIVE) {
    cell_revive(&(buffer_board[cell->pos_y][cell->pos_x]));
  }
}

void update_board_state()
{
  memcpy(buffer_board, main_board, sizeof(main_board));
  for (int y = 1; y < height_y - 1; y++){
    for (int x = 1; x < width_x -1; x++){
      change_cell_state(&(main_board[y][x]),check_cell_neighbors(&(main_board[y][x])));
    }
  }
  memcpy(main_board, buffer_board, sizeof(main_board));
}

