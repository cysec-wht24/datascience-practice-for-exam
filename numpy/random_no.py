import numpy as np

rng = np.random.default_rng(seed=1) # Seed is just the starting point for a random number generator.

print(rng.integers(low=1, high=101, size=(3, 2)))

rng2 = np.random.default_rng()

fruits = np.array(["🍎", "🍊", "🍌", "🥥", "🍍"])
fruits = rng2.choice(fruits, size=(3, 3))
print(fruits)