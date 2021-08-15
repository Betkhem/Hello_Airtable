import requests

def lambda_handler():
    AIRTABLE_BASE_ID = "shrp5Xhe3bkzWkkhz"
    AIRTABLE_TABLE_NAME = "tblX1jGmYZoqyHrlE"
    endpoint = "https://api.airtable.com/v0/appS2PargbyUuC55c/MainTable"
    
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
    r = requests.get(endpoint, json=data, headers=headers)
    a = []
    res = r.json()
    b = [res['records'][i]['fields']['title'] for i in range(len(res['records']))]
    return b
