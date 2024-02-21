import pandas as pd
import numpy as np

ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2024', periods=1000))

ts.cumsum()

ts.cumsum().plot(kind="line");

x = np.random.rand(10, 4)
df = pd.DataFrame(x, columns=['a', 'b', 'c', 'd'])
df.plot.bar();
