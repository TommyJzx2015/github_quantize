import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({
        'A' : ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
        'B' : ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
        'C' : np.random.randn(8),
        'D' : np.random.randn(8)}
)
result = df.groupby("B").mean()
result.plot()
plt.plot(result)
plt.show()
