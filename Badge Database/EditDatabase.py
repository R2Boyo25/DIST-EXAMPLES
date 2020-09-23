
import json
import os


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
            json.dump(self.db , open(self.location, "w+"), indent=4)
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
            print("No Value Can Be Found for " + str(key))
            #return False

    def delete(self , key):
        if not key in self.db:
            return False
        del self.db[key]
        self.dumpdb()
        return True

    def resetdb(self):
        self.db={}
        self.dumpdb()
        return True
from tkinter import *
from tkinter import ttk
#from database import Database
x = Database("BadgeDB.json")
with open(str(x.location)) as json_file:
    data = json.load(json_file)
def calculate(*args):
    value2=DBVAR2.get()
    value=(DBVAR.get())
    value=value.lower()
    keys=[]
    for key in data.keys():
        keys.append(key)
    if value == 'help':
        databaseoutput.set('Type the name in the first box, and the value in the second')
    elif value =='list':
        databaseoutput.set(','.join(keys))

    else:
        if value in keys:
            databaseoutput.set('Name {} already used.'.format(value))
        else:
            x.set(value, value2)
            #a=x.location
            #print(x.location)
            databaseoutput.set('Successfully Written to {}'.format(str(x.location)))

root = Tk()
root.title("Add To {}".format(x.location))
#root.pack(fill=X, expand = True)
#root.geometry("1200x600")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.pack(fill=X, expand = True)
root.columnconfigure(2, weight=3)
root.rowconfigure(0, weight=1)

DBVAR2 = StringVar(root, value='Help')
DBVAR = StringVar(root, value='Help')
databaseoutput = StringVar(value='Press Add To Database To Use')

DBFINDENTRY = ttk.Entry(mainframe, width=7, textvariable=DBVAR)
DBFINDENTRY.grid(column=2, row=1, sticky=(W, E))
DBFINDENTRY2 = ttk.Entry(mainframe, width=7, textvariable=DBVAR2)
DBFINDENTRY2.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=databaseoutput).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Add To Database", command=calculate).grid(column=2, row=5, sticky=W)

ttk.Label(mainframe, text="Name:").grid(column=1, row=1, sticky=W)
ttk.Label(mainframe, text="Value:").grid(column=1, row=2, sticky=E)
#ttk.Label(mainframe, text='Test').grid(column=2, row=2, sticky=W)

def check23(e=None):
    value=(DBVAR.get())
    value=value.lower()
    keys=[]
    for key in data.keys():
        keys.append(key)
    if value in keys:
        databaseoutput.set('Name {} already used.'.format(value))
    else:
        databaseoutput.set('Press Add To Database To Use')
DBFINDENTRY.focus()
root.bind('<Return>', calculate)
root.bind('<KeyRelease>', check23)

root.mainloop()