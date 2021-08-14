import requests

def lambda_handler(event, context):
    AIRTABLE_BASE_ID = "appfYvHhxoN5sQjm8"
    AIRTABLE_TABLE_NAME = "MainTable"
    endpoint = f"https://api.airtable.com/v0/{AIRTABLE_BASE_ID}/{AIRTABLE_TABLE_NAME}"
    
    headers = {
        "Authorization":"Bearer keyGBZTg6leNOpAxw",
        "Content-Type": "application/json",
    }
    data = {
      "records": [
        {
          "fields": {
            "ID": 1,
            "title": "Проверка 1"
          }
        },
        {
          "fields": {
            "ID": 2,
            "title": "Проверка 2"
          }
        }
      ]
    }
    r = requests.post(endpoint, json=data, headers=headers)
    return r.json()
