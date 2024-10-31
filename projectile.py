import matplotlib.pyplot as plt
import numpy as np

PI = np.pi


class Projectile:
    def __init__(self, v0, theta, g=9.8):
        """
        Initialize the projectile with initial velocity (v0), launch angle (theta) in degrees,
        and acceleration due to gravity (g).
        """
        self.v0 = v0
        self.theta = np.radians(theta)  # Convert angle to radians
        self.g = g

    def __call__(self, t: float) -> tuple[float, float]:
        """Get the position at a given time t."""
        return self.position(t)

    def position(self, t: float) -> tuple[float, float]:
        """Calculate the projectile's position at time t."""
        x = self.v0 * np.cos(self.theta) * t
        y = self.v0 * np.sin(self.theta) * t - 0.5 * self.g * t**2
        return np.round(x, 2), np.round(y, 2)

    def velocity(self, t: float) -> tuple[float, float]:
        """Calculate the projectile's velocity at time t."""
        vx = self.v0 * np.cos(self.theta)
        vy = self.v0 * np.sin(self.theta) - self.g * t
        return np.round(vx, 2), np.round(vy, 2)

    def horizontal_range(self) -> float:
        """Calculate the horizontal range of the projectile."""
        return np.round((self.v0**2 * np.sin(2 * self.theta)) / self.g, 2)

    def time_of_flight(self) -> float:
        """Calculate the time of flight of the projectile."""
        return np.round((2 * self.v0 * np.sin(self.theta)) / self.g, 2)

    def maximum_height(self) -> float:
        """Calculate the maximum height reached by the projectile."""
        return np.round((self.v0**2 * np.sin(self.theta) ** 2) / (2 * self.g), 2)

    def plot_trajectory(
        self,
        dt=0.01,
        velocity_vector=True,
        components=True,
        time_instant=0,
        projectile_color="red",
        velocity_color="green",
        x_velocity_color="blue",
        y_velocity_color="orange",
    ):
        """Plot the trajectory of the projectile."""
        self.check_valid_time_instant(time_instant)
        t_values = np.arange(0, self.time_of_flight(), dt)
        x_values, y_values = zip(*[self.position(t) for t in t_values])

        plt.plot(x_values, y_values, color="black", zorder=1, label="Trajectory")
        plt.plot(
            *self.position(time_instant),
            ".",
            color=projectile_color,
            zorder=3,
            markersize=20,
            label="Projectile",
        )
        plt.xlabel("$x$")
        plt.ylabel("$y$")
        plt.title(f"Projectile at t = {time_instant}s")

        if velocity_vector:
            self.plot_velocity_vector(time_instant, velocity_color)
            if components:
                self.plot_velocity_components(
                    time_instant, x_velocity_color, y_velocity_color
                )

        plt.legend(fontsize=8)
        plt.show()

    def plot_velocity_vector(self, t, color):
        """Plot the velocity vector at a given time."""
        x, y = self.position(t)
        vx, vy = self.velocity(t)
        plt.quiver(
            x,
            y,
            vx,
            vy,
            angles="xy",
            scale_units="xy",
            scale=1,
            color=color,
            zorder=2,
            label="Velocity",
        )

    def plot_velocity_components(self, t, x_color, y_color):
        """Plot the x and y components of the velocity at a given time."""
        x, y = self.position(t)
        vx, vy = self.velocity(t)
        plt.quiver(
            x,
            y,
            vx,
            0,
            angles="xy",
            scale_units="xy",
            scale=1,
            color=x_color,
            zorder=2,
            label="Vx",
        )
        plt.quiver(
            x,
            y,
            0,
            vy,
            angles="xy",
            scale_units="xy",
            scale=1,
            color=y_color,
            zorder=2,
            label="Vy",
        )

    def check_valid_time_instant(self, time_instant: float):
        """Ensure the provided time instant is within the flight time range."""
        if not (0 <= time_instant <= self.time_of_flight()):
            raise ValueError(
                f"Time must be within [0, {self.time_of_flight()}] seconds."
            )
