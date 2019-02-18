import os
import requests
from pprint import pprint
auth = ('carthorse-cjw296', os.environ.get('GITHUB_TOKEN'))
# what's the in the env?
response = requests.get('https://api.github.com/repos/cjw296/playground/commits/master/status',
                        auth=auth)
data = response.json()
pprint(data['state'])

for status in data['statuses']:
    pprint(status)
