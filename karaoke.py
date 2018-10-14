#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from smallsmilhandler import SmallSMILHandler


class KaraokeLocal(SmallSMILHandler):

    def __init__(self, fichero):
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        parser.parse(fichero)
        self.lista = sHandler.get_tags()

    def __str__(self):
        self.cadena = ""
        for dic in self.lista:
            atributos = list(dic)
            self.linea = ""

            for atributo in atributos:
                if atributo != "Etiqueta" and dic[atributo] != "":
                    self.linea += atributo + '= "'
                    self.linea += dic[atributo] + '"' + "\t"
            self.cadena += (dic["Etiqueta"] + "\t" + self.linea + "\n")
        return self.cadena

    def to_json(self):
        fichero_json = json.dumps(karaoke.lista)
        fichero2 = open("karaoke.json", "w")
        fichero2.write(fichero_json)

    def do_local(self):
        for dic in self.lista:
            atributos = list(dic)
            for atributo in atributos:
                if atributo == "src" and dic[atributo][:7] == "http://":
                    url = dic["src"]
                    nombre_fich = url[url.rfind("/")+1:]
                    urllib.request.urlretrieve(url, nombre_fich)
                    dic[atributo] = nombre_fich
        return self.lista


if __name__ == "__main__":

    try:
        fichero = open(sys.argv[1])

    except IndexError:
        print("Usage: python3 karaoke.py file.smil")

    karaoke = KaraokeLocal(fichero)
    print(karaoke)
    karaoke.to_json()
    karaoke.do_local()
    print(karaoke)
