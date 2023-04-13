import requests
import json
import os

def update_choices():
    r = requests.get("http://176.62.187.250/implement.php")


    implement = json.loads(r.text)

    with open("implement.json", "w") as f:
        json.dump(implement, f)

    r = requests.get("http://176.62.187.250/shape.php")


    shape = json.loads(r.text)

    with open("shape.json", "w") as f:
        json.dump(shape, f)


    r = requests.get("http://176.62.187.250/glazing.php")


    glazing = json.loads(r.text)


    with open("glazing.json", "w") as f:
        json.dump(glazing, f)



    os.system("./venv/bin/python manage.py makemigrations")

    os.system("./venv/bin/python manage.py migrate")