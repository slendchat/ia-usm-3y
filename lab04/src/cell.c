#include "../inc/cell.h"

void cell_die(cell_entity* cell){
  cell->cell_type = DEAD;
}
void cell_revive(cell_entity* cell){
  cell->cell_type = ALIVE;
}