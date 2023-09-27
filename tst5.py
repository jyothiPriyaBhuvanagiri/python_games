import json
import logging
from tb_rest_client.rest_client_ce import *
from tb_rest_client.rest import ApiException

url = 'http://134.109.4.9:8080'

username = "tenant@thingsboard.org"
password = "tenant43"

data_file = "dev_data_test2.json"

with open(data_file, 'r') as file:
    data = json.load(file)

    for item in data:
        name = item.get('device', {}).get('name', None)

    with RestClientCE(base_url=url) as rest_client:
        try:
            rest_client.login(username=username, password=password)
            for item in data:
                name = item.get('device', {}).get('name', None)
                description = item.get('device', {}).get('description', None)
                tags = item.get('device', {}).get('tags', None)
                print(tags, object)

                if name:
                    # Creating the first device
                    device = Device(name=name, type="thermometer",
                                    device_profile_id=DeviceProfileId('38077f30-4c89-11ee-82d6-998155b2e069',
                                                                      'DEVICE_PROFILE'),
                                    additional_info={"description": description
                        }, customer_id=CustomerId('db57c5a0-4b30-11ee-bb2a-8d91617a135d', 'CUSTOMER')
                                    )

                    device = rest_client.save_device(device)
                    logging.info("Device 1 was created:\n%r\n", device)

        except ApiException as e:
            logging.exception(e)
