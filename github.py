import os
import requests
from pprint import pprint
auth = ('carthorse-cjw296', os.environ.get('GITHUB_TOKEN'))
# what's the in the env?
pprint({k: v for (k, v) in os.environ.items() if not k.endswith('TOKEN')})

response = requests.get('https://api.github.com/repos/cjw296/playground/commits/master/status',
                        auth=auth)
pprint(response.json())
