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
        return np.round(x, 2), np.round(y, 2)

    def velocity(self, t):
        vx = self.v0 * np.cos(self.theta)
        vy = self.v0 * np.sin(self.theta) - self.g * t
        return np.round(vx), np.round(vy)

    def horizontal_range(self):
        R = (self.v0**2 * np.sin(2 * self.theta)) / self.g
        return np.round(R, 2)

    def time_of_flight(self):
        t_f = (2 * self.v0 * np.sin(self.theta)) / self.g
        return np.round(t_f, 2)

    def maximum_height(self):
        h_max = (self.v0 * np.sin(self.theta) ** 2) / (2 * self.g)
        return np.round(h_max, 2)
