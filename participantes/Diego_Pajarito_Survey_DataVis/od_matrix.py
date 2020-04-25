import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import get_data


answers = get_data.get_survey_Data()

# Plot 1: start/end trip
path = 'plots/changes_groups.png'
od_data = answers.groupby(['localidadOrigin', 'localidadDestination'], as_index=False)
od_data = od_data['timestamp'].count()
cmap = sns.cubehelix_palette(dark=.3, light=.8, as_cmap=True)
ax = sns.scatterplot('localidadDestination', 'localidadOrigin', data=od_data, size='timestamp', sizes=(1, 300),
                     cmap=cmap, legend=False)
# ax.set(xlabel='Origen del viaje', ylabel='Destino', title='', fontsize=30)
ax.set_ylabel('Localidad de origen', fontsize=6);
ax.set_xlabel('Localidad de destino', fontsize=6);
ax.tick_params(labelsize=5)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.tight_layout()
plt.show()
plt.savefig(path)

plt.close()
