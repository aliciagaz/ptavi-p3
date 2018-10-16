#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.diccionario = {
                "root_layout": ["width", "height", "background-color"],
                "region": ["id", "op", "bottom", "left", "right"],
                "img": ["src", "region", "begin", "dur"],
                "audio": ["src", "begin", "dur"],
                "textstream": ["src", "region"]}
        self.lista = []

    def startElement(self, name, attrs):
        dic = {}
        if name in self.diccionario:
            dic["Etiqueta"] = name
            for atributos in self.diccionario[name]:
                dic[atributos] = attrs.get(atributos, "")
            self.lista.append(dic)

    def get_tags(self):
        return self.lista


if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
