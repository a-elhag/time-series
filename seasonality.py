from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np

data = np.array([5384, 8081, 10282, 9156, 6118, 9139, 12460, 10717, 7825,
             9693, 15177, 10990])

data_period_avg = np.zeros((4,1))

for period in range(4):
    data_period_avg[period] = data[period::4].mean()

data_table = np.hstack((np.arange(4).reshape(4,-1), data.reshape(4,3),
                       data_period_avg.reshape(4,-1)))

headers = ["Period", "Cycle 1", "Cycle 2", "Cycle 3", "Average"]
table = tabulate(data_table, headers, tablefmt="fancy_grid")
print(table)


