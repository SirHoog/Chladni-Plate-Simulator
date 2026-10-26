import time

import numpy as np

import matplotlib.pyplot as plt
import matplotlib.animation as animation

class Sim:
    def __init__(self, size=100, n=500):
        self.size = size
        self.grid = np.zeros((size, size))
        self.n    = n # Number of particles
        self.particles = np.random.rand(self.n, 2) * self.size

        self.last = time.perf_counter() # Track the last time per frame update

    def _update(self, dt):
        # Random motion for now
        self.particles += np.random.randn(self.n, 2) * dt
        self.particles = np.clip(self.particles, 0, self.size)

    def run(self, interval=int(1000/60)):
        fig, ax = plt.subplots()
        ax.axis('off')
        ax.imshow(self.grid, cmap='gray')
        sc = ax.scatter(self.particles[:, 1], self.particles[:, 0], c='w', s=5)

        def update(frame):
            now = time.perf_counter()
            dt = now - self.last
            self.last = now
            self._update(dt)

            sc.set_offsets(self.particles[:, ::-1])
            ax.set_title(f"FPS: {1/dt:.2f}")

            return sc,

        ani = animation.FuncAnimation(fig, update, interval=interval, cache_frame_data=False)
        plt.show()