# Chargement des variables d'environnement à partir du fichier .env
set -a
[ -f .env ] && . .env
set +a

docker run -d --name elastic \
    -v "$ELASTIC_DATA_DIR" \
    --net elastic \
    -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.17.10