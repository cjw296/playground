import os
from requests import Session
from pprint import pprint

travis = Session()
travis.headers['Travis-API-Version'] = '3'
travis.headers['Authorization'] = 'token '+os.environ.get('TRAVIS_TOKEN')
response = travis.get('https://api.travis-ci.org/repo/cjw296%2Fplayground')
pprint(response.json())

if os.environ.get('DO_RELEASE'):
    print('Doing release!')
else:
    print('Triggering release')
    response = travis.post('https://api.travis-ci.org/repo/cjw296%2Fplayground/requests', json={
      "request": {
        "message": "Releasing 0.1.2",
        "branch": os.environ.get('TRAVIS_COMMIT'),
        "config": {
          "env": {
            "DO_RELEASE": "true"
          },
          "after_success": [],
        }
      }
    })
