from elasticsearch import Elasticsearch
import pandas as pd

# Connexion à Elasticsearch
es = Elasticsearch([{'host': 'localhost', 'port': 9200,'scheme': 'http'}])


def get_sentiment_distribution(es,patient_firstname, patient_lastname):
    query = {
            "size": 10,
            "query": {
                "bool": {
                    "must": [
                        {"term": {"patient_firstname": patient_firstname}},
                        {"term": {"patient_lastname": patient_lastname}}
                    ]
                }
            },
            "aggs": {
                "sentiment_distribution": {
                    "terms": {"field": "emotion"}
                }
            }
        }
    

    response = es.search(index="notes", body=query)
    print(response)
    buckets = response["aggregations"]["sentiment_distribution"]["buckets"]

    df = pd.DataFrame(buckets, columns=["key", "doc_count"])
    return df

print(get_sentiment_distribution(es,'Samantha','Smith'))

