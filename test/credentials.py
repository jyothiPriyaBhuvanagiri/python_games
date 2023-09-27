import requests

url = 'http://134.109.4.9:8080/api/device/27dbf140-5d4b-11ee-82d6-998155b2e069/credentials'
headers = {
    'accept': 'application/json',
    'X-Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJ0ZW5hbnRAdGhpbmdzYm9hcmQub3JnIiwidXNlcklkIjoiZGFmODhlYTAtNGIzMC0xMWVlLWJiMmEtOGQ5MTYxN2ExMzVkIiwic2NvcGVzIjpbIlRFTkFOVF9BRE1JTiJdLCJzZXNzaW9uSWQiOiI1ZjQ2ZmQxMS05ZTA3LTQ1MjEtYWVmYS1iOTQwMDgxN2YyOTQiLCJpc3MiOiJ0aGluZ3Nib2FyZC5pbyIsImlhdCI6MTY5NTgyODg1MywiZXhwIjoxNjk1ODM3ODUzLCJlbmFibGVkIjp0cnVlLCJpc1B1YmxpYyI6ZmFsc2UsInRlbmFudElkIjoiZDk3YzAwYzAtNGIzMC0xMWVlLWJiMmEtOGQ5MTYxN2ExMzVkIiwiY3VzdG9tZXJJZCI6IjEzODE0MDAwLTFkZDItMTFiMi04MDgwLTgwODA4MDgwODA4MCJ9.4MT2ocVoVmIaf4K6UUX_UXH1gCEoqIZdclqARBizuJ7WzxLGH-btSszDTN-TWzE3Ol0G4ry8cSLmJJ2ynN6V1A'
}

response = requests.get(url, headers=headers)

# Check the response
if response.status_code == 200:
    data = response.json()
    credentials_id = data.get('credentialsId')
    if credentials_id is not None:
        with open("credentials_id.txt", "w") as file:
            file.write(credentials_id)
            print(f"credentialsId: {credentials_id} written to credentials_id.txt")
    print(data)
else:
    print(f"Request failed with status code: {response.status_code}")
