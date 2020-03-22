import pandas as pd
pd.__version__
pd.set_option('display.max_columns', None)
# first look at people
peoples = pd.read_csv('Archivos CSV/PersonasEODH2019.csv', sep=';')
print(f'{len(peoples):} respondants') #66819
people_healthcare    =  peoples[peoples.p6_id_ocupacion.isin([17])]
people_other_essential = peoples[peoples.p6_id_ocupacion.isin([4,5,8,9])]
percent_healthcare = len(people_healthcare.p6_id_ocupacion)*100/len(peoples)
percent_other_essential = len(people_other_essential.p6_id_ocupacion)*100/len(peoples)

print(f'{percent_healthcare:.2f}% in healthcare, {percent_other_essential:.2f}% in other essential services')

# now look at trips
trips = pd.read_csv('Archivos CSV/ViajesEODH2019.csv', sep=';')
print(f'{len(trips):} trips reported')

pub_transit = trips[trips.modo_principal.isin(['TransMilenio', 'SITP Zonal', 'SITP Provisional', 'Alimentador'])]
pub_transit_work_and_work_travel = pub_transit[pub_transit.p17_Id_motivo_viaje.isin([1,2])]
pub_transit_needcare = pub_transit[pub_transit.p17_Id_motivo_viaje.isin([4])]
pub_transit_consumer = pub_transit[pub_transit.p17_Id_motivo_viaje.isin([10])]
pub_transit_caretraker = pub_transit[pub_transit.p17_Id_motivo_viaje.isin([15])]

percent_transit = len(pub_transit)*100/len(trips)
percent_transit_work_and_work_travel = len(pub_transit_work_and_work_travel)*100/len(pub_transit)
percent_transit_needcare = len(pub_transit_needcare)*100/len(pub_transit)
percent_transit_consumer = len(pub_transit_consumer)*100/len(pub_transit)
percent_transit_caretraker = len(pub_transit_caretraker)*100/len(pub_transit)

percent_essential_work = percent_transit_work_and_work_travel*((percent_healthcare+percent_other_essential)/100);
print(f'{percent_transit:.2f}% trips taken with public transit')
# print(f'{percent_transit_work_and_work_travel:.2f}% of public transit is currently work related')
print(f'{percent_essential_work:.2f}% of public transit is currently ESSENTIAL work related')
print(f'{percent_transit_needcare:.2f}% of publ transit is people in need of care')
print(f'{percent_transit_consumer:.2f}% of public transit is for consumers')
print(f'{percent_transit_caretraker:.2f}% of public transit is to take care of someone')

percent_using_still = percent_essential_work+percent_transit_needcare+percent_transit_consumer+percent_transit_caretraker;
print(f'{percent_using_still:}% capacity')

