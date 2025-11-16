import pandas as pd

logs = pd.DataFrame({
    'id': [1, 2, 3, 4, 5, 6, 7],
    'num': [1, 1, 1, 2, 1, 2, 2]
})

logs['prev'] = logs['num'].shift(1)
logs['next'] = logs['num'].shift(-1)


result = logs[
    (logs['num'] == logs['prev']) &
    (logs['num'] == logs['next'])

][['num']].drop_duplicates().rename(columns={'num': 'ConsecutiveNums'})

print(result)

