import numpy as np

arr = np.array([
    [1, np.nan, 3],
    [4, 5, np.nan],
    [7, 8, 9]
])

# Compute column-wise mean, ignoring NaN
col_means = np.nanmean(arr, axis=0)

# Find indices where values are NaN
inds = np.where(np.isnan(arr))

print(inds) # only for showing array

# Replace NaNs with the corresponding column mean
arr[inds] = np.take(col_means, inds[1])

print(arr)
