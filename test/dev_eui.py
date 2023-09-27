import requests

url = 'http://134.109.5.110:8090/api/devices?limit=10&offset=0&applicationId=9debbb59-d4d6-4306-8141-f25029222bca'

headers = {
    'accept': 'application/json',
    'Grpc-Metadata-Authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJjaGlycHN0YWNrIiwiaXNzIjoiY2hpcnBzdGFjayIsInN1YiI6ImQ4NWYyYmMzLTkwYzYtNDJkNC05NjQyLTNhMDVjMGY4ZDI3NiIsInR5cCI6ImtleSJ9.boT3F7JJa17K-nAStL24jePBpHgpfnNVR2pYvilTQmE"
}

response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    data = response.json()
    dev_eui_list = [item['devEui'] for item in data.get('result', [])]

    # Write the devEui values to a text file
    with open("dev_eui.txt", "w") as file:
        for dev_eui in dev_eui_list:
            file.write(dev_eui + '\n')

    print("Data written to dev_eui.txt")
else:
    print(f"Request failed with status code: {response.status_code}")
