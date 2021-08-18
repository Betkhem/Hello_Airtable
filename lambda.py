import requests

def lambda_handler(event, context):
    endpoint = "https://api.airtable.com/v0/appS2PargbyUuC55c/MainTable"
    
    headers = {
        "Authorization":"Bearer keyGBZTg6leNOpAxw",
        "Content-Type": "application/json",
    }
    data = {
        "records": [
            {
                "id": "rec7yqd3qgWKb3C3L",
                "fields": {
                    "ID": 1,
                    "title": "Проверка 1"
                },
                "createdTime": "2021-08-15T16:58:24.000Z"
            },
            {
                "id": "recqfBklgbBUZxegE",
                "fields": {
                    "ID": 2,
                    "title": "Проверка 2"
                },
                "createdTime": "2021-08-15T16:58:24.000Z"
            },
            {
                "id": "recMSRE5shQZgx9TG",
                "fields": {
                    "ID": 3,
                    "title": "Проверка 3"
                },
                "createdTime": "2021-08-15T16:58:24.000Z"
            }
        ],
        "offset": "recMSRE5shQZgx9TG"
    }
    r = requests.get(endpoint, json=data, headers=headers)
    res = r.json()
    c = [(res['records'][i]['fields']['ID'], res['records'][i]['fields']['title']) for i in range(len(res['records']))] #collect title and ID fields 
    d = [c[i][1] for i in range(len(c))] # array of titles
    for i in range(len(c)): # list of title values ordered by Id column
        if c[i][0] == 1:
            d[0] = d[0].replace(d[0], c[i][1], 1)
        d[c[i][0] - 1] = d[c[i][0] - 1].replace(d[c[i][0] -1 ], c[i][1])
    c = []
    for i in range(len(d)): # algorithm creates list of 3 elements form title field, and adds that list to "c"
        k = []
        if i == 0:
            for j in range(3):
                k.append(d[j])
        elif i == len(d) - 1:
            for j in range(2):
                k.append(d[-2+j])
            k.append(d[0])
        else:
            k.append(d[i-1])
            k.append(d[i])
            k.append(d[i+1])
        c.append(k)
    return str(c)
