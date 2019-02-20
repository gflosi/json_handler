import json


class Model:
    def __init__(self):
        self.data_json = json.loads(open('textos.txt').read())

        # self.d = {}
        self.dic_tmp = {}

        json_data = self.data_json['TEXTOITINERARIO']['ES']

        if type(json_data) == str:
            self.data_json['TEXTOITINERARIO']['tmp'] = "tmp"
        else:
            self.dic_tmp.update(self.create_node_tmp(json_data))
            self.data_json['TEXTOITINERARIO']['tmp'] = self.dic_tmp

        print(self.data_json)

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
