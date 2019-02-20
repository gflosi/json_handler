import json
from model import Model


class Controller:
    def __init__(self):
        self.modelo = Model()

    def duplicate_node(self, param):
        self.modelo.duplicate_node(param)
