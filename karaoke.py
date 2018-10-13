#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import json
import urllib.request
from xml.sax import make_parser
from smallsmilhandler import SmallSMILHandler



if __name__ == "__main__":
    try:
        parser = make_parser()
        sHandler = SmallSMILHandler()
        parser.setContentHandler(sHandler)
        fichero = open("karaoke.smil")
        parser.parse(fichero)
        lista = sHandler.get_tags()
        fichero_json = json.dumps(lista)
        fichero2 = open("karaoke.json", "w") 
        fichero2.write("fichero_json")
        
        for dic in lista:
            atributos = list(dic) 
            linea = ""
            for atributo in atributos:
                if atributo != "Etiqueta" and dic[atributo] != "":
                    linea += atributo + '= "'
                    linea += dic[atributo] + '"' + "\t"                    
                    if atributo == "src" and dic[atributo][:7] == "http://":
                        url =dic["src"]
                        print(url)
                        nombre_fich= "ali"
                        urllib.request.urlretrieve(url, nombre_fich)
            print(dic["Etiqueta"] + "\t" + linea + "\n")
             
        
        
        
    except IndexError:
        sys.exit("Usage: python3 karaoke.py file.smil")
        