import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import get_data


answers = get_data.get_survey_Data()

# Bar 1: Changes by age group
path = 'plots/changes_age.png'
change_data = answers.groupby(['age', 'changeForeseen'], as_index=False)
change_data = change_data['timestamp'].count()
change_data.columns = ['Edad', 'change', 'count']
change_data = change_data[change_data['count'] > 1]
ax = sns.barplot('count', 'change', data=change_data, hue='Edad', palette='BuGn_r',
                 hue_order=['Mayor a 60', 'Entre 51 y 60', 'Entre 41 y 50', 'Entre 31 y 40',
                            'Entre 21 y 30', ' Menor a 20'])
# ax.set(xlabel='Origen del viaje', ylabel='Destino', title='', fontsize=30)
ax.set_ylabel('', fontsize=6);
ax.set_xlabel('Respuestas', fontsize=6);
ax.tick_params(labelsize=7)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
# plt.title('Una vez termine esta cuarentena, usted cree que..')
plt.tight_layout()
plt.show()
plt.savefig(path)
plt.close()



# Bar 2: Changes by estrato group
path = 'plots/changes_estrato.png'
change_data = answers.groupby(['estrato', 'changeForeseen'], as_index=False)
change_data = change_data['timestamp'].count()
change_data.columns = ['Estrato', 'change', 'count']
change_data = change_data[change_data['count'] > 1]
ax = sns.barplot('count', 'change', hue='Estrato', data=change_data, palette='GnBu_d')
# ax.set(xlabel='Origen del viaje', ylabel='Destino', title='', fontsize=30)
ax.set_ylabel('', fontsize=6);
ax.set_xlabel('Respuestas', fontsize=6);
ax.tick_params(labelsize=7)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
# plt.title('Una vez termine esta cuarentena, usted cree que..')
plt.tight_layout()
plt.show()
plt.savefig(path)
plt.close()



# Bar 1: Changes by bicyle use group
path = 'plots/changes_bicicleta.png'
change_data = answers.groupby(['bicycleEmergency', 'changeForeseen'], as_index=False)
change_data = change_data['timestamp'].count()
change_data.columns = ['Bicicleta Prestada', 'change', 'count']
change_data = change_data[change_data['Bicicleta Prestada'] == 'Sí']
ax = sns.barplot('count', 'change', data=change_data, palette='GnBu_d')
ax.set_ylabel('', fontsize=6)
ax.set_xlabel('Respuestas', fontsize=6)
ax.tick_params(labelsize=7)
ax.set_xticklabels(ax.get_xticklabels(), rotation=90)
plt.title('Usuarios Bicicleta Emergencia')
plt.tight_layout()
plt.show()
plt.savefig(path)
plt.close()
