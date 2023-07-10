docker run -d --name elastic \
    -v /home/apprenant/elastic/psycho_nlp_data \
    --net elastic \
    -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.17.10