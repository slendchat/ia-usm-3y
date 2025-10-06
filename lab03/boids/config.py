from dataclasses import dataclass

@dataclass
class Config:
  SCREEN_WIDTH:int = 1600
  SCREEN_HEIGHT:int = 900

  MAX_FPS:int = 60

  weight_separation:float = 1.3
  weight_alignment:float = 1.4
  weight_coherence:float = 1.2

  view_radius: float = 150.0

  max_force: float = 80.0
  max_speed: float = 360.0
  min_speed: float = 120.0
  friction: float = 0.98

  EPS = 1e-6

@dataclass
class Colors:
  BLUE  = (0, 0, 255)
  RED   = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)