from dataclasses import dataclass

@dataclass
class Config:
  SCREEN_WIDTH:int = 800
  SCREEN_HEIGHT:int = 600

  MAX_FPS:int = 60

  weight_separation:float = 2.0
  weight_alignment:float = 0.9
  weight_coherence:float = 0.9

  view_radius = 50

  max_force:int = 100
  max_speed:int = 50
  friction:float = 0.9

  EPS = 1e-6

@dataclass
class Colors:
  BLUE  = (0, 0, 255)
  RED   = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)