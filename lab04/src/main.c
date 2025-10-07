#include <stdio.h>
#include <unistd.h>
#include <time.h>
#include <stdlib.h>

#include "../inc/cell.h"
#include "../inc/board.h"
#include "../inc/render.h"
#include "../inc/rules.h"
#include "../inc/utils.h"


int main()
{
  // init plain board
  init_board();

  // Generate some alive cells on the board
  srand(time(NULL));
  for (int y = 1; y < height_y - 1; y++) {
    for (int x = 1; x < width_x - 1; x++) {
      int noise = (rand() % 100) < 2; 
      int alive_neighbors = 0;

        for (int dy = -1; dy <= 1; dy++) {
          for (int dx = -1; dx <= 1; dx++) {
            if (dy == 0 && dx == 0) continue;
              if (main_board[y + dy][x + dx].cell_type == ALIVE) {
                alive_neighbors++;
              }
          }
        }

      int clustering = (alive_neighbors > 0 && alive_neighbors <= 2 && (rand() % 100) < 25);

      if (noise || clustering) {
        cell_revive(&main_board[y][x]);
      }
    }
  }



  // MAIN LOOP
  for (;;){

    draw_frame(main_board);
    
    update_board_state();
    
    sleep_ms(50);

  }

  return 0;
}