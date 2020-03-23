import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

sns.set()

covid_data = pd.read_csv('Covid19_hubei.csv')
covid_data = covid_data.dropna(subset=['age'])

ages = covid_data.age
has_symbols = ages.str.contains('-')

sns.distplot(ages[~has_symbols])
plt.show()