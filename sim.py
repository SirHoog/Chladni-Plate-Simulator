import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Sim:
    def __init__(self, size=100, n=500):
        self.size = size
        self.grid = np.zeros((size, size))
        self.n    = n # Number of particles
        self.particles = np.random.rand(self.n, 2) * self.size

    def _update(self, dt):
        # Random motion for now
        self.particles += np.random.randn(self.n, 2) * dt
        self.particles = np.clip(self.particles, 0, self.size)

    def run(self, frames=100, interval=1):
        fig, ax = plt.subplots()
        ax.axis('off')
        ax.imshow(self.grid, cmap='gray')
        sc = ax.scatter(self.particles[:, 1], self.particles[:, 0], c='r', s=1)

        def update(frame):
            self._update(1)
            sc.set_offsets(self.particles[:, ::-1])
            ax.set_title(f"Frame {frame}")
            return sc,

        ani = animation.FuncAnimation(fig, update, frames=frames, interval=interval)
        plt.show()