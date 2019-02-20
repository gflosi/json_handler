import json
from model import Model


class Controller:
    def __init__(self, file_name):
        self.modelo = Model(file_name)

    def duplicate_node(self, param):
        self.modelo.duplicate_node(param)

    def tmp_node(self):
        self.modelo.tmp_node()
