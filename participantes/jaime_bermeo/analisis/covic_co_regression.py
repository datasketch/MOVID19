import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

sns.set()

co_data = pd.read_csv('co_cases_cleaned.csv')

prediction = 101.74*np.sqrt(np.linspace(0, 20, 1000)) - 135.15
df = pd.DataFrame({'day': np.linspace(0, 20, 1000), 'forecast': prediction})

fig, ax = plt.subplots()
sns.regplot(x='day', y='cases', data=co_data, x_estimator=np.mean, logx=False, ax=ax)
# sns.lineplot(x='day', y='forecast', data=df, ax=ax)
# sns.scatterplot(x='day', y='cases', data=co_data, ax=ax)
ax.set_xlim(0, 15)
ax.set_ylim(0, 260)

# figure = sns.lmplot(x='day', y='cases', data=co_data, fit_reg=True, order=2, ci=None)
# figure.set(xlim=(0, 50))

plt.show()