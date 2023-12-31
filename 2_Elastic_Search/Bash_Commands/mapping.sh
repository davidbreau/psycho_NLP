curl -X PUT "localhost:9200/notes" -H 'Content-Type: application/json' -d'
{
    "settings": {
        "index": {
            "analysis": {  
                "analyzer": {
                    "my_analyzer": {
                        "type": "standard"
                    }
                }
            }
        }
    },
    "mappings": {
        "properties": {
        "patient_lastname": {
            "type": "keyword"
        },
        "patient_firstname": {
            "type": "keyword"
        },
        "text": {
            "type": "text",
            "analyzer": "standard"
        },
        "date": {
            "type": "date"
        },
        "patient_left": {
            "type": "boolean"
        },
        "Emotion": {
            "type": "keyword"
        },
        "confidence": {
            "type": "float"
        }
        }
    }
}
'