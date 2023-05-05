# import requests
# import json

# r = requests.get("http://176.62.187.250/service.php?s_code=7364-0554")

# data = json.loads(r.text)


# print(data)


# import json

with open("test.txt", "rb") as f:
    d = f.read()


print(list(d))
