
import urllib.request
import json
import os

# Prepare the input data
data = {
    "Inputs": {
        "WebServiceInput0":
        [
            {
                    'id':1136817,
                    'week':1,
                    'center_id':11,
                    'meal_id':2631,
                    'checkout_price':251.5,
                    'base_price':251.5,
                    'emailer_for_promotion':0,
                    'homepage_featured':0,
                    'num_orders':77,
            },
        ],
    },
    "GlobalParameters":  {
    }
}
body = str.encode(json.dumps(data))
headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ key)}
req = urllib.request.Request(endpoint, body, headers)

try:
    response = urllib.request.urlopen(req)
    result = response.read()
    json_result = json.loads(result)
    y = json_result["Results"]["WebServiceOutput0"][0]["predicted_orders"]
    print('Predicted orders: {:.2f}'.format(y))

except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers to help debug the error
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
