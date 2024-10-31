import numpy as np

PI = np.pi


class Projectile:
    def __init__(self, v0, theta, g=9.8):
        self.v0 = v0
        self.theta = theta
        self.g = g

    def position(self, t):
        x = self.v0 * np.cos(self.theta) * t
        y = self.v0 * np.sin(self.theta) * t - (1 / 2) * self.g * t**2
        return x, y

    def velocity(self, t):
        vx = self.v0 * np.cos(self.theta)
        vy = self.v0 * np.sin(self.theta) - self.g * t
        return vx, vy

    def horizontal_range(self):
        return (self.v0**2 * np.sin(2 * self.theta)) / self.g

    def time_of_flight(self):
        return (2 * self.v0 * np.sin(self.theta)) / self.g

    def maximum_height(self):
        return (self.v0 * np.sin(self.theta) ** 2) / (2 * self.g)
