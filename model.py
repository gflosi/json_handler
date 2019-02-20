import json


class Model:
    def __init__(self):
        self.data_json = json.loads(open('textos.txt').read())
        self.dic_tmp = {}

    def create_node_tmp(self, node):
        array_aux = {}

        for key, value in node.items():
           try:
               if len(node.items()) > 0:
                   array_aux.update({key: self.create_node_tmp(node[key])}.copy())
           except:
                node_aux = {key: "tmp"}.copy()
                array_aux.update(node_aux)

        return array_aux

    def duplicate_node(self, param):
        # json_data = self.data_json['TEXTOITINERARIO']['ES']

        json_data = self.return_node(0, param)

        if type(json_data) == str:
            self.insert_tmp_node(self.return_node(1, param), "tmp")
        else:
            self.dic_tmp.update(self.create_node_tmp(json_data))
            self.insert_tmp_node(self.return_node(1, param), self.dic_tmp)

        print(self.data_json)

    def return_node(self, index, param):
        param = param[::-1]
        count = len(param) - 1
        node = self.data_json

        while count >= index:
            node = node[str(param[count])]
            count -= 1

        return node

    def insert_tmp_node(self, node, text):
        node["tmp"] = text