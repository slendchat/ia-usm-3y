#pragma once
int check_cell_neighbors(cell_entity *cell);
void change_cell_state(cell_entity *cell, int alive_neghbors);
void update_board_state();
