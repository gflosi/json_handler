import json


class Controller:
    def __init__(self):
        data = json.loads(open('textos.txt').read())
        for key, value in data["SUBJECT"].items():
            print(key)

        # print(data[0]["EN"])
