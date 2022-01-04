import json

class DB:
    def __init__(self,dbfile,drdbfile):
        self.dbfile = dbfile
        self.drdbfile = drdbfile

    def refresh_db(self):
        with open(self.dbfile, encoding="UTF-8") as fd:
            self.db = json.load(fd)

        with open(self.drdbfile, encoding="UTF-8") as fdr:
            self.drdb = json.load(fdr)

        return self.db, self.drdb

    def add_db_hoca_alti(self,item,item1,val):

        self.refresh_db()
        self.db[item][0][item1] = val
        with open(self.dbfile,"w", encoding="UTF-8") as fe:
            json.dump(self.db,fe,indent = 4)

        self.refresh_db()

    def del_db_hoca_alti(self,item,item1):

        self.refresh_db()
        self.db[item][0].pop(item1)
        with open(self.dbfile,"w", encoding="UTF-8") as fe:
            json.dump(self.db,fe,indent = 4)

        self.refresh_db()

    def add_db_hoca(self,db,item):

        self.refresh_db()

        self.db[item]= []
        with open(db,"w", encoding="UTF-8") as fe:
            json.dump(self.db,fe,indent = 4)

        self.refresh_db()
