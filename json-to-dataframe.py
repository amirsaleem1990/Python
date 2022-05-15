name = 'a.json'
import json
import pandas as pd
from pandas.io.json import json_normalize

with open(name) as f:
    data = json.load(f)
df = pd.DataFrame.from_dict(json_normalize(data['features']), orient='columns')
df.head()