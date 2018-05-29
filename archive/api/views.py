from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from elasticsearch import Elasticsearch

def test(request):
    print('wtf')
    return HttpResponse('wer')

def compare_price(request):
    print('twsaf')
    data = request.GET
    print('data: ',data)
    item = data['item']
    #size, price, item
    item_car = {k:v for k,v in data.items()}
    #size, price, title, productBrand, item
    item_hon = get_item(item)
    res = {
      'honestbee': item_hon,
      'carrefour': item_car 
    } 
    return JsonResponse(res)

def get_item(item):
    es = Elasticsearch(
      hosts=[{'host': '127.0.0.1', 'port': 9200}],
    )
    res = es.search(index='honestbee',
      doc_type='carrefour',
      body={
        "query": {
          "match": {
            "title": {
              "query":     item,
              "fuzziness": "AUTO"
            }
          }
        }
    })

    res = res['hits']['hits'][0]['_source']
    res = {i:res[i] for i in ['title','productBrand','size','price']}
    res['item'] = '%s%s'%(res['productBrand'],res['title'])
    #print('res: ',res)
    return res
