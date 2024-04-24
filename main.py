import pandas as pd

df = pd.DataFrame({'A': [[1, 2, 3], [4, 5], [6]], 'B': ['foo', 'bar', 'baz']})
x = df.explode('A')
print(x)