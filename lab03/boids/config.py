from dataclasses import dataclass

@dataclass
class Config:
  SCREEN_WIDTH:int = 800
  SCREEN_HEIGHT:int = 600

  MAX_FPS:int = 60

  weight_separation:float = 1.5
  weight_alignment:float = 1.0
  weight_coherence:float = 1.5

  view_radius: float = 80.0

  max_force: float = 60.0
  max_speed: float = 250.0
  min_speed: float = 60.0
  friction: float = 0.98

  EPS = 1e-6

@dataclass
class Colors:
  BLUE  = (0, 0, 255)
  RED   = (255, 0, 0)
  GREEN = (0, 255, 0)
  BLACK = (0, 0, 0)
  WHITE = (255, 255, 255)