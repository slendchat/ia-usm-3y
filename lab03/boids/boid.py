from __future__ import annotations

from math import atan2, cos, pi, sin
from random import uniform

from pygame import Vector2

from config import Config


class Boid:

    @staticmethod
    def _limit(v: Vector2, m: float) -> Vector2:
        if m > 0 and v.length_squared() > m * m:
            v.scale_to_length(m)
        return v

    @staticmethod
    def _w_t(d: float, R: float) -> float:
        t = 1.0 - d / R
        return t if t > 0.0 else 0.1

    def __init__(self, pos: Vector2):
        self.pos: Vector2 = pos
        self.velocity: Vector2 = Vector2(uniform(-1, 1), uniform(-1, 1))
        if self.velocity.length_squared() == 0:
            self.velocity = Vector2(1, 0)
        self.velocity = self.velocity.normalize() * (0.5 * Config.max_speed)
        self.acceleration = Vector2()
        self.neighbors: list[tuple["Boid", float]] = []

    def sense_neighbors(self, all_boids: list["Boid"]):
        self.neighbors = []
        view_radius_sq = Config.view_radius ** 2
        for boid in all_boids:
            if boid is self:
                continue
            distance_sq = (boid.pos - self.pos).length_squared()
            if distance_sq <= view_radius_sq:
                self.neighbors.append((boid, distance_sq))

    def _count_force_separation(self) -> Vector2:
        steer = Vector2()
        for other, d_sq in self.neighbors:
            if d_sq <= Config.EPS:
                continue
            steer += (self.pos - other.pos) / (d_sq + Config.EPS)
        if steer.length_squared() == 0:
            return Vector2()
        desired = steer.normalize() * Config.max_speed
        return self._limit(desired - self.velocity, Config.max_force)

    def _count_force_alignment(self) -> Vector2:
        radius = Config.view_radius
        weighted_velocity = Vector2()
        weight_sum = 0.0
        for other, d_sq in self.neighbors:
            distance = d_sq ** 0.5
            weight = self._w_t(distance, radius)
            if weight <= 0.0:
                continue
            weighted_velocity += other.velocity * weight
            weight_sum += weight
        if weight_sum == 0.0:
            return Vector2()
        average_velocity = weighted_velocity / weight_sum
        if average_velocity.length_squared() == 0.0:
            return Vector2()
        desired = average_velocity.normalize() * Config.max_speed
        return self._limit(desired - self.velocity, Config.max_force)

    def _count_force_cohesion(self) -> Vector2:
        radius = Config.view_radius
        center = Vector2()
        weight_sum = 0.0
        for other, d_sq in self.neighbors:
            distance = d_sq ** 0.5
            weight = self._w_t(distance, radius)
            if weight <= 0.0:
                continue
            center += other.pos * weight
            weight_sum += weight
        if weight_sum == 0.0:
            return Vector2()
        center /= weight_sum
        direction = center - self.pos
        if direction.length_squared() == 0.0:
            return Vector2()
        desired = direction.normalize() * Config.max_speed
        return self._limit(desired - self.velocity, Config.max_force)

    def count_result_vector(self):
        if not self.neighbors:
            self.acceleration = Vector2()
            return

        separation = self._count_force_separation()
        alignment = self._count_force_alignment()
        cohesion = self._count_force_cohesion()

        steer = (
            Config.weight_separation * separation
            + Config.weight_alignment * alignment
            + Config.weight_coherence * cohesion
        )
        self.acceleration = self._limit(steer, Config.max_force)

    def update(self, dt: float):
        if dt <= 0.0:
            return

        self.velocity += self.acceleration * dt
        self._limit(self.velocity, Config.max_speed)
        self.velocity *= Config.friction

        speed = self.velocity.length()
        if speed < Config.min_speed:
            if speed <= Config.EPS:
                self.velocity = Vector2(uniform(-1, 1), uniform(-1, 1))
                if self.velocity.length_squared() == 0.0:
                    self.velocity = Vector2(1, 0)
                self.velocity = self.velocity.normalize() * Config.min_speed
            else:
                self.velocity.scale_to_length(Config.min_speed)

        self.pos += self.velocity * dt

        width, height = Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT
        if self.pos.x < 0.0:
            self.pos.x = 0.0
            if self.velocity.x < 0.0:
                self.velocity.x *= -1
        elif self.pos.x > width:
            self.pos.x = width
            if self.velocity.x > 0.0:
                self.velocity.x *= -1

        if self.pos.y < 0.0:
            self.pos.y = 0.0
            if self.velocity.y < 0.0:
                self.velocity.y *= -1
        elif self.pos.y > height:
            self.pos.y = height
            if self.velocity.y > 0.0:
                self.velocity.y *= -1

        self.acceleration = Vector2()

    def get_vertices(self, size: int = 10) -> list[tuple[float, float]]:
        v = self.velocity
        if v.length_squared() == 0.0:
            v = Vector2(1, 0)
        ang = atan2(v.y, v.x)
        a = 0.75 * pi
        px, py = self.pos.x, self.pos.y

        x0 = px + size * cos(ang)
        y0 = py + size * sin(ang)
        x1 = px + size * cos(ang + a)
        y1 = py + size * sin(ang + a)
        x2 = px + size * cos(ang - a)
        y2 = py + size * sin(ang - a)

        return [(x0, y0), (x1, y1), (x2, y2)]
