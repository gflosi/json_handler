import json
import copy
import yaml


class Model:
    def __init__(self):
        self.data_json = json.loads(open('textos.txt').read())

        self.d = {}
        self.dic_tmp = {}

        json_data = self.data_json['TABLAITINERARIO']['ES']

        self.dic_tmp.update(self.create_node_tmp(json_data))

        self.data_json['TABLAITINERARIO']['tmp'] = self.dic_tmp

        print(self.data_json)

    def create_node_tmp(self, node):
        d = {}
        dic_tmp = {}

        for key, value in node.items():
            try:
                if (len(node.items()) > 0):
                    dic_tmp.update({key: self.create_node_tmp(node[key])}.copy())
            except:
                d = {key: "tmp"}.copy()
                dic_tmp.update(d)

        return dic_tmp
