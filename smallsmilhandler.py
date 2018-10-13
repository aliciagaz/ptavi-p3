#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler


class SmallSMILHandler(ContentHandler):
    
    
    def __init__ (self):
        
        self.root_layout = " "
        self.root_layout_width = " "
        self.root_layout_height = " "
        self.root_layout_background_color = " "
        self.region = " "
        self.region_id = " "
        self.region_top = " "
        self.region_bottom = " "
        self.region_left = " "
        self.region_right = " "
        self.img = " "
        self.img_src = " "
        self.img_region = " "
        self.img_begin = " "
        self.img_dur = " "
        self.audio = " "
        self.audio_src = " "
        self.audio_begin = " "
        self.audio_dur = " "
        self.textstream = " "
        self.textstream_src = " "
        self.textstream_region = " "
        self.lista = []
        self.diccionario = {}
        self.diccionario_etiqueta = {}
        
    def startElement(self, name, attrs):
        """
        Método que se llama cuando se abre una etiqueta
        """
        self.diccionario = {}
        self.diccionario_etiqueta = {}
        
        if name == "root-layout":
            # De esta manera tomamos los valores de los atributos
            self.diccionario["Etiqueta"] = name
            self.root_layout_width = attrs.get("width", "")
            self.root_layout_height = attrs.get("height", "")
            self.root_layout_background_color = attrs.get("background_color", "")
            self.diccionario["width"] = self.root_layout_width
            self.diccionario["height"] = self.root_layout_height
            self.diccionario["background_color"] = self.root_layout_background_color
            self.lista.append(self.diccionario)
            
            
        elif name == "region":
            self.diccionario["Etiqueta"] = name
            self.region_id = attrs.get("id", "")
            self.region_top = attrs.get("top", "")
            self.region_bottom = attrs.get("bottom", "")
            self.region_left = attrs.get("left", "")
            self.region_right = attrs.get("right", "")
            self.diccionario["id"] = self.region_id
            self.diccionario["top"] = self.region_top
            self.diccionario["bottom"] = self.root_layout_background_color
            self.diccionario["left"] = self.region_left
            self.diccionario["right"] = self.region_right
            self.lista.append(self.diccionario)
            
        elif name == "img":
            self.diccionario["Etiqueta"] = name
            self.img_src = attrs.get("src", "")
            self.img_region = attrs.get("region", "")
            self.img_begin = attrs.get("begin", "")
            self.img_dur = attrs.get("dur", "")
            self.diccionario["src"] = self.img_src
            self.diccionario["region"] = self.img_region
            self.diccionario["begin"] = self.img_begin
            self.diccionario["dur"] = self.img_dur
            self.lista.append(self.diccionario)
    
        elif name == "audio":
            self.diccionario["Etiqueta"] = name
            self.audio_src = attrs.get("src", "")
            self.audio_begin = attrs.get("begin", "")
            self.audio_dur = attrs.get("dur", "")
            self.diccionario["src"] = self.audio_src
            self.diccionario["begin"] = self.audio_begin
            self.diccionario["dur"] = self.audio_dur
            self.lista.append(self.diccionario)
            
        elif name == "textstream":
            self.diccionario["Etiqueta"] = name
            self.textstream_src = attrs.get("src", "")
            self.textstream_region = attrs.get("region", "")
            self.diccionario["src"] = self.textstream_src
            self.diccionario["region"] = self.textstream_region
            self.lista.append(self.diccionario)

    def get_tags (self):
        
        return self.lista
        
        
        
if __name__ == "__main__":
    """
    Programa principal
    """
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open('karaoke.smil'))
    print(cHandler.get_tags())
    