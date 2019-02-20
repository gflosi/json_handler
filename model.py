import json
import yaml
from time import gmtime, strftime

class Model:
    def __init__(self, file_name):
        self.data_json = json.loads(open(file_name).read())
        self.dic_tmp = {}

        self.default_text = self.build_default_text
        self.tmp_json_node = {}

    def create_node_tmp(self, node):
        array_aux = {}

        for key, value in node.items():
           try:
               if len(node.items()) > 0:
                   array_aux.update({key: self.create_node_tmp(node[key])}.copy())
           except:
                node_aux = {key: self.default_text}.copy()
                array_aux.update(node_aux)

        return array_aux

    def duplicate_node(self, param):
        json_data = self.return_node(0, param)

        if type(json_data) == str:
            self.insert_tmp_node(self.return_node(1, param), self.default_text)
        else:
            self.dic_tmp.update(self.create_node_tmp(json_data))
            self.insert_tmp_node(self.return_node(1, param), self.dic_tmp)

        #print(yaml.dump(self.data_json))

    def return_node(self, step_back, param):
        # build the node according to a list of parameters
        # backs the json node if desired

        param = param[::-1]
        count = len(param) - 1
        node = self.data_json

        while count >= step_back:
            node = node[str(param[count])]
            count -= 1

        return node

    def insert_tmp_node(self, node, text):
        node[self.default_text] = text

    def build_default_text(self):
        return strftime("tmp%Y%m%d%H%M%Stmp", gmtime())

    def tmp_node(self):
        self.tmp_node_rec(self.data_json)

    def tmp_node_rec(self, node):
        for key, value in node.items():
            if key == self.default_text:
                self.tmp_json_node = node[key]
                break
            try:
                if len(node.items()) > 0:
                    self.return_temp_node_rec(node[key])
            except:
                pass

    def edit_node(self, param, value):
        self.insert_tmp_node(self.return_node(0, param), value)

    def remove_node(self, param, value):
        # del self.insert_tmp_node(self.return_node(0, param), value)
