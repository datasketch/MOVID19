import pandas as pd
import geopandas
from time import gmtime, strftime

survey_file = 'data/Form_Responses.csv'
survey_names = ['timestamp', 'gender', 'age', 'estrato', 'localidadOrigin', 'localidadDestination', 'hourOrigin',
                'hourDestination', 'tripMeanBefore', 'costBefore', 'changeForeseen', 'tripMeanForeseen',
                'routineForeseen', 'changes90Days', 'tripMean90Days', 'bicycleApp', 'routine90', 'bicycleEmergency',
                'position', 'scheduleNight', 'whyBicycle', 'whyYesBicycle', 'whyN0Bicycle', 'transportNoBicycle',
                'tripMeanNoBicycle', 'bicycleSuggestion', 'open']
localidades_file = 'data/localidades.geojson'


def get_survey_Data():
    survey_data = pd.read_csv(survey_file)
    survey_data.columns = survey_names
    survey_data['hourOrigin'] = pd.to_datetime(survey_data['hourOrigin'])
    survey_data['hourDestination'] = pd.to_datetime(survey_data['hourDestination'])
    return survey_data


def get_localidades():
    localidades_data = geopandas.read_file(localidades_file)
    return localidades_data
