import json


class Controller:
    def __init__(self):
        data = json.loads(open('textos.txt').read())
        print(data["SUBJECT"]["EN"])
