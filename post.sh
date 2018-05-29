for entry in data/*.json
do
    #cat $entry | jq -r '.products| .[]' | curl -d @- -H 'Content-Type: application/json' -XPOST 127.0.0.1:9200/honestbee/carrefour  
    cat $entry | jq -r '.products'
done
