import requests


r = requests.get("http://176.62.187.250/implement.php")


print(r.text)