def sum_to_n(arr, n):
    res = []
    for a in arr:
        for b in range(round(len(arr) / 2)):
            if a + arr[b] == n:
                res.append([a, arr[b]])
    return res


# print(sum_to_n([1, 2, 3, 4],5))
# print(sum_to_n([1, 4, 5, 3, 2],6))
# print(sum_to_n([1, 2, 5, 6, 3],7))

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
desired_width=320
pd.set_option('display.width', desired_width)

pd.set_option('display.max_columns',10)
data = pd.read_csv(r"C:\Users\jonas\Documents\UQ\COMP4702\Homework\HW01\Book1.csv")
print(data.head())
print(data.describe())
print(data.corr())
print(data.cov())
plt.imshow(data.corr())
plt.show()

