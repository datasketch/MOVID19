import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt

sns.set()

covid_data = pd.read_csv('Covid19_hubei.csv')
covid_data = covid_data.dropna(subset=['symptoms'])

symptoms = covid_data.symptoms

has_fever = symptoms.str.contains('fever')
has_cough = symptoms.str.contains('cough')
has_chills = symptoms.str.contains('chills')
has_pneumonia = symptoms.str.contains('pneumonia')

target_symptoms = (has_fever, has_cough, has_chills, has_pneumonia)

symptoms_labels = np.array(['Fiebre', 'Tos', 'Resfriado', 'Neumonía', 'Otros'])
symptoms_count = np.array([covid_data[condition].shape[0] for condition in target_symptoms])
other_symptoms_count = covid_data[~has_fever & ~has_cough & ~has_chills & ~has_pneumonia]
symptoms_count = np.append(symptoms_count, other_symptoms_count.shape[0])


plot_data = pd.DataFrame({'Síntomas': symptoms_labels, 'No. de pacientes': symptoms_count})
sns.catplot(x='Síntomas', y='No. de pacientes', kind='bar', data=plot_data)
plt.show()
