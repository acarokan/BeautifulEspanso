import json
from strings import dbfile

class DB:
    def __init__(self,dbfile):
        self.dbfile = dbfile

    def get_db(self):
        with open(self.dbfile, encoding="UTF-8") as f:
            db = json.load(f)
        return db

    def get_drs_ids(self):
        db = self.get_db()
        return list(db.keys())

    def write_db(self,db):
        with open(self.dbfile,"w", encoding="UTF-8") as f:
            json.dump(db,f,indent = 4)

    def get_kisaltma_from_id(self,id):
        db = self.get_db()
        return db[id]["kisaltmalar"]

    def get_all_dr_isim(self):
        dr_isim_list = []
        db = self.get_db()
        for i in db.keys():
            dr_isim_list.append(db[i]["isim"])
        return dr_isim_list

    def get_all_kisaltmalar(self):
        all_kisaltmalar = {}
        db = self.get_db()
        for i in db.keys():
            all_kisaltmalar.update(db[i]["kisaltmalar"])
        return all_kisaltmalar
        
    def add_dr_db(self,data):
        db = self.get_db()
        id = self.get_drs_ids()
        id = int(id[-1])+1
        id = str(id)
        db[id] = data
        self.write_db(db)

    def add_kisaltma_db(self,id,data):
        db = self.get_db()
        db[id]["kisaltmalar"].update(data)
        self.write_db(db)

    def fix_dr(self,id,data):
        db = self.get_db()
        db[id]["isim"] = data
        self.write_db(db)

    def fix_kisaltma(self,id,data):
        db = self.get_db()
        db[id][kisaltmalar].update(data)
        self.write_db(db)

    def remove_dr_db(self,id):
        db = self.get_db()
        db.pop(id)
        self.write_db(db)

    def remove_kisaltma_db(self,id,data):
        db = self.get_db()
        db[id]["kisaltmalar"].pop(data)
        self.write_db(db)

if __name__ == '__main__':
    db = DB(dbfile)
    data = {
    "isim": "okan acar",
    "kisaltmalar":{
    "vay": "vay vay vay"
    }
    }
    db.add_kisaltma_db("3",{"ekle":"ekledim ekledim"})
