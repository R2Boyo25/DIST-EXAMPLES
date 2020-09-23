import json
import os
from difflib import get_close_matches
def CMatches(input:str, keys):
    return get_close_matches(input, keys)
class Database(object):
    def __init__(self , location):
        self.location = os.path.expanduser(location)
        self.load(self.location)

    def load(self , location):
       if os.path.exists(location):
           self._load()
       else:
            self.db = {}
       return True

    def _load(self):
        self.db = json.load(open(self.location , "r"))

    def dumpdb(self):
        try:
            json.dump(self.db , open(self.location, "w+"))
            return True
        except:
            return False

    def set(self , key , value):
        try:
            self.db[str(key)] = value
            self.dumpdb()
        except Exception as e:
            print("[X] Error Saving Values to Database : " + str(e))
            return False

    def get(self , key):
        try:
            return self.db[key]
        except KeyError:
            BadgeInfo.set('Value Not in Database')
            print("No Value Can Be Found for " + str(key))

            #return False

    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

    def resetdb(self):
        #self.db={}
        #self.dumpdb()
        return True
from tkinter import *
from tkinter import ttk
#from database import Database
x = Database("BadgeDB.json")

with open(x.location) as json_file:
    data = json.load(json_file)
    #print(data)
def calculate(*args):

    try:
        value = str(DBVAR.get())
        value=value.lower()
        keys=[]
        for key in data.keys():
            keys.append(str(key.lower()))
        #print(keys)
        UKeys=[]
        for item in keys:
            UKeys.append(item.title())
            #print(item)
        #for k in x.keys():
        #    keys.append('{}'.format(k.title()))
        #if value in db:
        #    BadgeInfo.set(db[value])
        if value in keys:
            BadgeInfo.set(x.get(value.lower()))
        elif value=='list':
            #keys=[]
            #for k in x.keys():
            #    keys.append('{}'.format(k.title()))
            BadgeInfo.set('List of Keys(capitalization does not matter):\n{}'.format(', '.join(UKeys)))
        else:

            #BadgeInfo.set('Not in The Database\nValid Terms(capitalization does not matter):\n{}, Or list (Lists Keys(Same as this))'.format(', '.join(UKeys)))
            BadgeInfo.set('Similar Entries:\n{}\nType list for a all entries'.format(CMatches(value, keys)))

    except ValueError:
        pass

root = Tk()
root.title("Read {} DataBase".format(x.location))
#root.pack(fill=X, expand = True)
#root.geometry("1200x600")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.pack(fill=X, expand = True)
root.columnconfigure(2, weight=3)
root.rowconfigure(0, weight=1)

DBVAR = StringVar(root, value='Help')
BadgeInfo = StringVar()

DBFINDENTRY = ttk.Entry(mainframe, width=7, textvariable=DBVAR)
DBFINDENTRY.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=BadgeInfo, wraplength=300, justify="center").grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Search Database", command=calculate).grid(column=2, row=5, sticky=W)

#ttk.Label(mainframe, text="DBVAR").grid(column=3, row=1, sticky=W)
#ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text=db['Yes']['no']).grid(column=2, row=2, sticky=W)

DBFINDENTRY.focus()
root.bind('<Return>', calculate)

root.mainloop()
