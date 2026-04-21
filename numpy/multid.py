import numpy as fuck
# needs to be homogenous
array = fuck.array([[['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']],
                    [['J', 'K', 'L'], ['M', 'N', 'O'], ['P', 'Q', 'R']],
                    [['S', 'T', 'U'], ['V', 'W', 'X'], ['Y', 'Z', ' ']]])

print(array.shape)
print(array[0][0][0]) # chain indexing
print(array[0, 0, 0]) # multidimensional indexing - faster

word = array[0,0,0] + array[2,0,0] + array[2,0,0]
print(word) 