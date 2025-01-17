import requests

details = (requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")).json()

#print(details) #for Complete Details of the API response.

for i in range(len(details)):
    print(details[i]["user"]["login"])

#print("Response:",response.json())

