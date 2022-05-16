import requests
import json



print("input site id")
site_id = input() # MLA
print("input seller id")
seller_id = input() # 179571326
response = requests.get("https://api.mercadolibre.com/sites/" + site_id + "/search?seller_id=" + seller_id)


if(response.status_code == 200):
    r = response.json()
    #parseo de query


json_object = json.dumps(r, indent = 4)
  
with open("output.json", "w") as outfile:
    outfile.write(json_object)