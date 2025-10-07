#pragma once

typedef enum _cell_status{
    DEAD = 0,
    ALIVE,
    WALL
}cell_status;

typedef struct {
    cell_status cell_type;
    int pos_x;
    int pos_y;
} cell_entity;

void cell_die(cell_entity* cell);
void cell_revive(cell_entity* cell);