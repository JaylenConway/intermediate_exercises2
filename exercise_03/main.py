import numpy as np

np_list = np.random.rand(10)

mean = np.mean(np_list)
median = np.median(np_list)
std_dev = np.std(np_list)

print(np_list)
print(f'Mean: {mean}')
print(f'Median: {median}')
print(f'Standard Deviation: {std_dev}')