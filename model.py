import json
import yaml
from time import gmtime, strftime

class Model:
    def __init__(self):
        self.dic_tmp = {}
        self.default_text = self.build_default_text
        self.tmp_json_node = {}
        self.data_json = {}
        self.data_table = {}
        self.insertion_node = ""

    def initialize_json(self, file_name):
        self.data_json = json.loads(open(file_name).read())

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

    # def remove_node(self, param, value):
        # del self.insert_tmp_node(self.return_node(0, param), value)

    def initialize_table(self, file_name):
        with open(file_name, "r") as ins:
            self.data_table = []
            for line in ins:
                self.data_table.append(line.replace("\n", '').split("|"))
        self.convert_array_to_json()

    def convert_array_to_json(self):
        for line in self.data_table:
            node_return = self.data_json
            position = 0
            for node in line:
                position += 1
                node_return = self.check_existance_node(node, node_return, position, len(line))

        print(self.data_json)

    def check_existance_node(self, node, node_return, position, length):
        try:
            return node_return[node]
        except:
            if position == length:
                node_return[self.insertion_node] = node
                return node_return[self.insertion_node]
            elif (length - position) == 1:
                node_return[node] = ""
                self.insertion_node = str(node)
                return node_return
            else:
                node_return[node] = {}

            return node_return[node]
