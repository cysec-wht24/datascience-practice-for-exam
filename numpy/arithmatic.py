import numpy as np

# Scalar arithmetic
array = np.array([1, 2, 3])

print(array + 1)
print(array - 2)
print(array * 3)
print(array / 4)
print(array ** 5)

print("Vectorized mmaths operations")
print(np.sqrt(array))
print(np.round(array))
print(np.pi)

print("element wise arithmatic")
# Element-wise arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print(array1 + array2)
print(array1 - array2)
print(array1 * array2)

print("Comparison operators")

scores = np.array([91, 55, 100, 73, 82, 64])

scores[scores < 60] = 0
print(scores)
