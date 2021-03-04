import json

with open('DiseaseData.json') as file:
    disease_data = json.load(file)


# for identify disease descripton and treatement
def disease_description(disease):
    return disease_data[disease]
