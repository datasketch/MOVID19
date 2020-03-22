import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

sns.set()

covid_data = pd.read_csv('Casos_co_220320.csv')
diagnostic_dates = covid_data.groupby('Fecha de diagnóstico')

grouped_data = covid_data.groupby(covid_data["Fecha de diagnóstico"].apply(pd.to_datetime).dt.date)
# grouped_data.count().cumsum()['Fecha de diagnóstico'].plot(kind="bar")
grouped_data.count().cumsum()['Fecha de diagnóstico'].plot(kind="hist")

data = grouped_data.count().cumsum()


plt.show()
