import time
from datetime import datetime

import pandas as pd
import requests

from schemas import JsonDataSchema


response = requests.get(
    'http://localhost:8000',
    params={'documents_date': int(time.time())},
)
data = JsonDataSchema(**response.json())
data_frame = (pd.DataFrame(columns=data.columns, data=data.rows)
              .rename(columns={'key1': 'document_id', 'key2': 'document_dt', 'key3': 'document_name'})
              .assign(load_dt=datetime.now()))
print(data_frame.to_dict('records'))
