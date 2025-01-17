# Dictionaries in Python

Dictionary are like JSON Format used to store collection of elements in the Form of Key-Value Pairs.
It Starts with {}

A List can Contain a Dictionary.
For example

ec2_instances = [
    {
        "id":1,
        "name":"t2.micro"
    },
    {
        "id":"2",
        "name": "t2.medium"
    },
    {
        "id": "3",
        "name":"t2.large"
    }
]



You can Speak with Github API using Python. Since Kubernetes has a Open Source Code.
1. Use The Request Module
2. Use API Call to make a Context.
3. JSON -> to a Dictionary Type. which is Closest one as we cannot work with Direct JSON objects.

GitHub Pull Request API Url.

For Kubernetes since it is Opensource You can find them on the Github itself
 [Kubernetes](https://github.com/kubernetes/kubernetes)

 For [Github API]()

 In python,
 To Fetch from the URL 
 
 ```python
 use import requests
 request.get(api.github.com/reponame/pulls)
 ```

 In Mathematics 