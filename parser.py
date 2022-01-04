#!/usr/bin/env python
#-*- coding: utf-8 -*-

from strings import *

class Parser():

    def __init__(self, file):
        super(Parser, self)
        self.list = {}
        self.file = open(file,"r",encoding="UTF-8")
        self.parse_file = self.file.read()
        self.file.close()

    def index_finder(self,content,strind):
        strind = str(strind)
        content = str(content)
        ind = content.index(strind) + len(strind)
        return ind

    def parse(self):
        self.content = self.parse_file
        start_index = self.index_finder(self.content,biz)
        self.content = self.parse_file[start_index:]
        while True:
            try:
                trigind = self.index_finder(self.content,trg)
                repind = self.index_finder(self.content,rep)
                trigstr = self.content[trigind: repind-len(rep)]
                self.content = self.content[trigind:]
                repstr = self.content[self.index_finder(self.content,rep): self.content.index(trg)]
                self.content = self.content[self.index_finder(self.content,repstr):]
                self.list[trigstr.rstrip("\"\n").lstrip("\":")] = repstr.rstrip("\"\n").lstrip("\":")
            except ValueError:
                trigstr = self.content[: self.content.index(rep)]
                repstr = self.content[self.index_finder(self.content,rep):]
                self.list[trigstr.rstrip("\"\n").lstrip("\":")] = repstr.rstrip("\"\n").lstrip("\":")
                break

        return self.list

if __name__ == '__main__':
    parser = Parser("default_yedek.yml")
    parser.parse()
