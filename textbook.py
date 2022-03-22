import json
mydict = {'insulator': 1}
with open('Insulator.json', 'w') as f:
    json.dump(mydict, f)