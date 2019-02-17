import os
from requests import Session
from pprint import pprint

travis = Session()
travis.headers['Travis-API-Version'] = '3'
travis.headers['Authorization'] = 'token '+os.environ.get('TRAVIS_TOKEN')
response = travis.get('https://api.travis-ci.org/repo/cjw296%2Fplayground')
pprint(response.json())
