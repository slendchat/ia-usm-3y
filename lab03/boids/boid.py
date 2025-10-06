from pygame import Vector2
from random import uniform
from config import Config
from math import atan2, cos, sin

class Boid():

  def __init__(self,pos:Vector2):
    self.pos:Vector2 = pos
    self.velocity:Vector2 = Vector2(uniform(-1,1), uniform(-1,1))
    if self.velocity.length_squared() == 0:
      self.velocity = Vector2(1,0)
    self.velocity = self.velocity.normalize() * (0.5 * Config.max_speed)
    self.acceleration = Vector2()

  def sense_neighbors(self, all_boids:list["Boid"]):
    neighbors = []
    for boid in all_boids:
      if boid == self:
        continue
      distance = (boid.pos - self.pos).length_squared()
      if distance < Config.view_radius:
        neighbors.append(boid, distance)
    return neighbors

  def _count_force_separation(self,neighbors:tuple):
    pass

  def _count_force_alignment(self,neighbors:tuple):
    pass

  def _count_force_cohesion(self,neighbors:tuple):
    pass

  def count_result_vector(self, neighbors:tuple):
    if neighbors.__len__ == 0:
      return

  def get_vertices(self, size:int = 10) -> tuple:
    self.pos.x = self.velocity.x
    self.pos.y = self.velocity.y
    v = self.velocity
    if v.length_squared() == 0:
      v = Vector2(1, 0)
    ang = atan2(v.y, v.x)
    a = 0.75 * 3.1415926535
    
    x0 = self.pos.x + size * cos(ang)
    y0 = self.pos.y + size * sin(ang)
    x1 = self.pos.x + size * cos(ang + a)
    y1 = self.pos.y + size * sin(ang + a)
    x2 = self.pos.x + size * cos(ang - a)
    y2 = self.pos.y + size * sin(ang - a)

    return [(x0,y0),(x1,y1),(x2,y2)]
