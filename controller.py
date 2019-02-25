import json
from model import Model


class Controller:
    def __init__(self, file_name, json, table):
        self.modelo = Model()
        if json is True:
            self.modelo.initialize_json(file_name)
        elif table is True:
            self.modelo.initialize_table(file_name)

    def duplicate_node(self, param):
        self.modelo.duplicate_node(param)

    def tmp_node(self):
        self.modelo.tmp_node()

    #def convert_table_to_node(self):
        #self.modelo.table_to_node()
