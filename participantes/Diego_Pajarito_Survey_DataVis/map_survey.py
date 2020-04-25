import geopandas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
from unidecode import unidecode
import get_data

# Map 1: From where did people reply
answers = get_data.get_survey_Data()
localidades = get_data.get_localidades()
answers = answers[['localidadOrigin', 'hourOrigin']]
answers.columns = ['localidad', 'hour']
answers = answers.groupby('localidad', as_index=False)
answers = answers['hour'].count()
answers.columns = ['localidad', 'answers']
answers['localidad'] = answers.apply(lambda x: unidecode(x['localidad'].lower()), axis=1)
localidades['localidad'] = localidades['LocNombre'].str.lower()
f, ax = plt.subplots(1)
base = localidades.plot(ax=ax, color='white', edgecolor='gray', linewidth=0.2)
geodata = localidades.merge(answers, how='left', left_on='localidad', right_on='localidad')
ax = geodata[geodata['answers'] > 0].plot(ax=base, column='answers', cmap='Greens', legend=True,
                                          legend_kwds={'label': 'Número de respuestas', 'orientation': 'horizontal'})
ax.set_axis_off()
plt.tight_layout()
plt.show()
plt.savefig('plots/map_surveys.png')
plt.close()

geodata.to_file('data/responses_localidad.json', driver='GeoJSON')
