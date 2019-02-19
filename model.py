import json
import copy
import yaml


class Model:
    def __init__(self):
        self.data_json = json.loads(open('textos.txt').read())

        self.data_json['TABLAITINERARIO']['tmp'] = ""

        self.d = {}
        self.dic_tmp = {}

        json_data = self.data_json['TABLAITINERARIO']['ES']

        self.dic_tmp.update(self.create_node_tmp(json_data))

        print ("FINAAAL")
        print(self.dic_tmp)
        #print(self.data_json)

        # self.data_json['TABLAITINERARIO']['TK'] = {"ok":"a", "ok2":"b"}

    def create_node_tmp(self, node):

        #print(node)

        d = {}
        dic_tmp = {}

        for key, value in node.items():
            try:
                if (len(node.items()) > 0):
                    dic_tmp.update({key: self.create_node_tmp(node[key])}.copy())
                    #(d)
                    print (dic_tmp)
                    #return self.create_node_tmp(node[key])
            except:
                d = {key: "tmp"}.copy()
                dic_tmp.update(d)
                print (dic_tmp)

        return dic_tmp
        #dic_tmp.update(d)


        #return dic_tmp

        #return node
