import numpy as np

num_list = []

num_list = list(map(int, input().split()))
p = np.prod(num_list)
print(p)