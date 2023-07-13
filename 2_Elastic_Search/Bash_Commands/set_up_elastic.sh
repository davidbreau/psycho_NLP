# # Chargement des variables d'environnement à partir du fichier .env
source "$(dirname "$0")/.env" #<--- ELASTIC_DATA_DIR = chemin complet vers miroir elastic search

docker run -d --name elastic \
    -v "$ELASTIC_DATA_DIR" \
    -p 127.0.0.1:9200:9200 -p 127.0.0.1:9300:9300 \
    -e "discovery.type=single-node" \
    docker.elastic.co/elasticsearch/elasticsearch:7.17.10