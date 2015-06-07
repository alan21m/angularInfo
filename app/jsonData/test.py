import json

with open('data/neighbors.json') as data_file:
    data = json.load(data_file)

ids = [u['id'] for u in data['nodes']]

params = '&'.join(['users=%s' % uid for uid in ids])
with open('data/ids.txt', 'w') as outfile:
    outfile.write(params)
