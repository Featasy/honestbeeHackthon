#curl -H 'Content-Type: application/json' -H 'Accept: application/vnd.honestbee+json;version=2' -H 'Accept-Language: zh-TW' -XGET https://core.honestbee.com/api/stores/10016/directory | curl -d @- -H 'Content-Type: application/json' -XPOST 127.0.0.1:9200/honestbee/carrefour

curl -H 'Content-Type: application/json' -H 'Accept: application/vnd.honestbee+json;version=2' -H 'Accept-Language: zh-TW' -XGET https://core.honestbee.com/api/stores/10016/directory | jq -r '.departments | .[].id' | 
while read line; do
    echo $line
    for page in {1..12}
    do
        echo $page
        curl -o "data/$line.$page.json" -H 'Content-Type: application/json' -H 'Accept: application/vnd.honestbee+json;version=2' -H 'Accept-Language: zh-TW' -XGET https://core.honestbee.com/api/departments/$line?page=$page&pageSize=500&sort=ranking
        sleep 1
    done
    echo '---------'
done 
