#!/usr/bin/env python
#-*- coding: utf-8 -*-

from strings import *

class Parser:
    def __init__(self, file):
        self.file = open(file,"r",encoding="UTF-8")
        self.file_content_list = self.file.readlines()
        self.file.close()
        self.data = {}
        self.parse()

    def parse(self,simge="|"):
        for i in self.file_content_list:
            kisaltma = i.split(simge)[0]
            karsilik = i.split(simge)[1]
            self.data.update({kisaltma: karsilik})

    def get_kisaltmalar(self):
        return list(self.data.keys())

    def get_kisaltmalar_text(self):
        txt = ""
        for i in self.data.keys():
            txt += "|"+ i
        return txt[1:]

    def get_karsiliklar(self):
        return list(self.data.values())

    def get_karsiliklar_text(self):
        txt = ""
        for i in self.data.values():
            txt += "|"+ i
        return txt[1:]

    def get_data(self):
        return self.data

if __name__ == '__main__':
    parser = Parser("default_yedek.yml")
    parser.parse()
