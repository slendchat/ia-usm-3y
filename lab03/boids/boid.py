from pygame import Vector2
from random import uniform
from config import Config
from math import atan2, cos, sin

class Boid():

  

  @staticmethod
  def _limit(v: Vector2, m: float) -> Vector2:
    if m > 0 and v.length_squared() > m*m:
      v.scale_to_length(m)
    return v

  @staticmethod
  def _w_t(d: float, R: float) -> float:
    # линейный спад [0..R] → [1..0]
    t = 1.0 - d / R
    return t if t > 0.0 else 0.0

  def __init__(self,pos:Vector2):
    self.pos:Vector2 = pos
    self.velocity:Vector2 = Vector2(uniform(-1,1), uniform(-1,1))
    if self.velocity.length_squared() == 0:
      self.velocity = Vector2(1,0)
    self.velocity = self.velocity.normalize() * (0.5 * Config.max_speed)
    self.acceleration = Vector2()

  def sense_neighbors(self, all_boids:list["Boid"]):
    self.neighbors = []
    for boid in all_boids:
      if boid == self:
        continue
      distance = (boid.pos - self.pos).length_squared()
      if distance < Config.view_radius:
        self.neighbors.append((boid, distance))

  def _count_force_separation(self):
    steer = Vector2()
    for other, d2 in self.neighbors:
      if d2 <= Config.EPS:      # сам себе не сосед
        continue
      # инверс-квадрат — сильнее при очень близком сближении
      steer += (self.pos - other.pos) / (d2 + Config.EPS)
    if steer.length_squared() == 0:
      return Vector2()
    desired = steer.normalize() * Config.max_speed
    return self._limit(desired - self.velocity, Config.max_force)

  def _count_force_alignment(self):
    R = Config.view_radius
    sum_v = Vector2()
    wsum = 0.0
    for other, d2 in self.neighbors:
      d = d2**0.5
      w = self._w_t(d, R)            # мягкий вес по расстоянию
      if w <= 0: 
        continue
      sum_v += other.velocity * w
      wsum  += w
    if wsum == 0 or sum_v.length_squared() == 0:
      return Vector2()
    desired = sum_v.normalize() * Config.max_speed
    return self._limit(desired - self.velocity, Config.max_force)

  def _count_force_cohesion(self):
    R = Config.view_radius
    center = Vector2()
    wsum = 0.0
    for other, d2 in self.neighbors:
      d = d2**0.5
      w = self._w_t(d, R)
      if w <= 0:
        continue
      center += other.pos * w
      wsum  += w
    if wsum == 0:
      return Vector2()
    center /= wsum
    to_c = center - self.pos
    if to_c.length_squared() == 0:
      return Vector2()
    desired = to_c.normalize() * Config.max_speed
    return self._limit(desired - self.velocity, Config.max_force)

  def count_result_vector(self):
    if self.neighbors.__len__ == 0:
      return
    
    a_sep = self._count_force_separation()
    a_aln = self._count_force_cohesion()
    a_coh = self._count_force_alignment()

    self.acceleration = self._limit(
      Config.weight_separation * a_sep +
      Config.weight_alignment  * a_aln +
      Config.weight_coherence  * a_coh,   # (название «coherence» у тебя, по классике «cohesion»)
      Config.max_force
    )


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
