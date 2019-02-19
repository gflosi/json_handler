import json
from pprint import pprint


class Controller:

    def __init__(self):
        with open('textos.json') as f:
            data = json.load(f)

        print(data)
