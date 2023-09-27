import requests
import json

# Read credentialsId from credentials_id.txt
with open("credentials_id.txt", "r") as credentials_file:
    credentials_id = credentials_file.read().strip()

# Read devEui values from dev_euis.txt
with open("dev_euis.txt", "r") as dev_euis_file:
    dev_euis = dev_euis_file.read().strip().split("\n")

# Iterate through devEui values and set ThingsBoardAccessToken for each device
for dev_eui in dev_euis:
    url = f"http://{host_url}/api/devices/{dev_eui}"
    cs_api_token = "{cs_api_token}"

    cs_headers = {
        "Authorization": f"Bearer {cs_api_token}",
        "content-type": "application/json"
    }

    cs_data = {
        "device": {
            "variables": {
                "ThingsBoardAccessToken": credentials_id
            }
        }
    }

    cs_response = requests.put(url, headers=cs_headers, data=json.dumps(cs_data))

    # Check the response
    if cs_response.status_code == 200:
        print(f"Device with devEui {dev_eui} updated successfully.")
    else:
        print(f"Failed to update device with devEui {dev_eui}. Status code: {cs_response.status_code}.")
