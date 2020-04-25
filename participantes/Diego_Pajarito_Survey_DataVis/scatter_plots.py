import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import get_data


answers = get_data.get_survey_Data()
answers['hourOrigin'] = answers['hourOrigin'].dt.hour + answers['hourOrigin'].dt.minute / 60
answers['hourDestination'] = answers['hourDestination'].dt.hour + answers['hourDestination'].dt.minute / 60

# Plot 1: start/end trip
path = 'plots/start_end_hours.png'
ax = sns.scatterplot('hourOrigin', 'hourDestination', data=answers, alpha=0.3, size=1, legend=False)
ax.set(xlabel='Hora de salida en la Mañana', ylabel='Hora de Salida en la Tarde / noche',
       title='Horarios de viaje')
ax.xaxis.set_major_locator(ticker.MultipleLocator(6))
ax.xaxis.set_major_formatter(ticker.ScalarFormatter())
ax.yaxis.set_major_locator(ticker.MultipleLocator(6))
ax.yaxis.set_major_formatter(ticker.ScalarFormatter())
plt.show()
plt.savefig(path)
plt.close()


# Plot 1: start, cost and gender
path = 'plots/start_end_gender.png'
answers = answers[answers['gender'].isin(['Hombre', 'Mujer', 'Mujer transgenero', 'Prefiero no decirlo',
                                          'Otro/no binario'])]
g = sns.FacetGrid(answers, col='gender')
g = g.map(plt.scatter, 'hourOrigin', 'hourDestination', alpha=0.3)
plt.show()
plt.savefig(path)
plt.close()

