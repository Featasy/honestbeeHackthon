import json
import glob
from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk

es = Elasticsearch(
  hosts=[{'host': '127.0.0.1', 'port': 9200}],
)

files = glob.glob('data/*.json')
for fi in files:
    with open(fi,'r') as f:
        data = json.load(f)
        data = data['products']
        bulk(es,data,index ='honestbee',doc_type='carrefour',raise_on_error = True)
