import pygame as pg
from game import Game
from boid import Boid
from pygame import Vector2
from random import randrange

def main():

  boids = list()

  for i in range(1,20):
    boids.append(Boid(Vector2(randrange(20,400), randrange(20,400))))

  game = Game()
  game.init()
  game.enter_game_loop(boids)


if __name__ == "__main__":
  main()