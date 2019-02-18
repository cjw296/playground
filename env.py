import os
from pprint import pprint
# what's the in the env?
pprint({k: v for (k, v) in os.environ.items() if not k.endswith('TOKEN')})
