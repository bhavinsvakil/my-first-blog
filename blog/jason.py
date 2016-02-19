import json
from pprint import pprint

with open('cucumber4.json') as data_file:    
    data = json.load(data_file)
    for feature in data:
        feature_name = feature['name']
        # print(feature_name)
        for element in feature['elements']:
            for step in element['steps']:
                status = step['result']['status']
                if status == 'failed':
                    print('feature name: ' + feature_name)
                    print('scenario name: ' + element['name'])
                    print('failure step name: ' + step['name'])
                if status == 'skipped':
                    print('feature name: ' + feature_name)
                    print('scenario name: ' + element['name'])
                    print('skipped step name: ' + step['name'])
