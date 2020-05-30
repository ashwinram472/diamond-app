import json
import pandas as pd

with open('mamba.json') as file:
    data = json.load(file)

print(data['results'][-1]['price'])

