import pygame as pg
import pygame_gui
from boid import Boid
from config import Config, Colors



class Game:
  def __init__(self):
    self._running = False
    self.size = self.width, self.height = Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT

  def draw_boid(self,boid_triangle:tuple):
    pg.draw.polygon(self._display_surf,Colors.BLACK,boid_triangle)

  def init(self):
    pg.init()
    self._running = True
    self.frames_per_sec = pg.time.Clock()
    self._display_surf = pg.display.set_mode(self.size)
    self._display_surf.fill(Colors.WHITE)
    pg.display.set_caption("Boids Game")

  def on_event(self, event):
    if event.type == pg.QUIT:
      self._running = False

  def on_loop(self, dt:float,boids:list["Boid"]):
    for b in boids:
      b.sense_neighbors(boids)

    for b in boids:
      b.count_result_vector()

  def on_render(self, dt:float, boids:list):
    self._display_surf.fill(Colors.WHITE)
    for boid in boids:
      self.draw_boid(boid.get_vertices())
    pg.display.update()

  def on_cleanup(self):
    pg.quit()

  def enter_game_loop(self, boids:list):
    while self._running == True:
      for event in pg.event.get():
        self.on_event(event)
      dt = min(self.frames_per_sec.tick(Config.MAX_FPS) / 1000.0, 1/30)

      self.on_loop(dt, boids)
      self.on_render(dt, boids)
    self.on_cleanup()