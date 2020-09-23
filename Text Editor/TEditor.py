# Importing Required libraries & Modules
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from os import path
import os
import subprocess
from pygments import lex
from pygments.lexers import PythonLexer
#mode='White'
#fontsize=config.fontsize
if not path.exists("TEconfig.py"):
  with open("TEconfig.py", "w") as File:
    File.write('#DARK or LIGHT or SEMIDARK\ncolormode="LIGHT"\nfontsize=15')
else:
  import TEconfig
  mode= TEconfig.colormode
  Fsize= TEconfig.fsize
#with open("TEconfig.txt", "r") as File:
#  for line in File:
#    print(line)
#    if 'color=black' in line:
#      mode='Black'
#      print('Darkmode')
#  for line in File:
#    if 'color=' not in line:
#      with open("TEconfig.txt", "w") as File:
#        File.write('color=white')

if mode=='DARK':
  mode='Black'
if mode=='SEMIDARK':
  mode='Gray'



# Defining TextEditor Class
class TextEditor:

  # Defining Constructor
  def __init__(self,root):
    # Assigning root
    self.root = root
    # Title of the window
    self.root.title("NoteBook-Basic")
    # Window Geometry
    self.root.geometry("1200x700+200+150")
    # Initializing filename
    self.filename = None
    # Declaring Title variable
    self.title = StringVar()
    # Declaring Status variable
    self.status = StringVar()

    def installPYIN():
      from subprocess import call
      call(['py', '-3', '-m', 'pip', 'install', '-U', 'python-dotenv'], shell=True)

    def run():
      path=self.title.get()
      #execfile(python3, str(path))
      #exec(open("{}".format(path)).read())
      print(path)
      #subprocess.call(['{}'.format(str(path))])
      os.startfile(path)

    def compiler():
      from subprocess import call
      path=self.title.get()
      call(['pyinstaller', '{}'.format(path)], shell=True)
    # Creating Titlebar
    self.titlebar = Label(self.root,textvariable=self.title,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
    # Packing Titlebar to root window
    self.titlebar.pack(side=TOP,fill=BOTH)
    # Calling Settitle Function
    self.settitle()
    if mode == 'Black':
      self.titlebar.configure(background='#1a1a1a',fg='#99ccff')
    if mode == 'Gray':
      self.titlebar.configure(background='black',fg='#f0f0f5')

    # Creating Statusbar
    self.statusbar = Label(self.root,textvariable=self.status,font=("times new roman",15,"bold"),bd=2,relief=GROOVE)
    # Packing status bar to root window
    self.statusbar.pack(side=BOTTOM,fill=BOTH)
    # Initializing Status
    self.status.set("Welcome To NoteBook")
    if mode == 'Black':
      self.statusbar.configure(background='#1a1a1a',fg='#99ccff')
    if mode == 'Gray':
      self.statusbar.configure(background='black',fg='#f0f0f5')

    # Creating Menubar
    self.menubar = Menu(self.root,font=("times new roman",15,"bold"),activebackground="skyblue")
    # Configuring menubar on root window
    self.root.config(menu=self.menubar)
    self.menubar.configure(background='#e0e0eb',fg='#99ccff')
    # Creating File Menu
    self.filemenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding New file Command
    self.filemenu.add_command(label="New",accelerator="Ctrl+N",command=self.newfile)
    # Adding Open file Command
    self.filemenu.add_command(label="Open",accelerator="Ctrl+O",command=self.openfile)
    # Adding Save File Command
    self.filemenu.add_command(label="Save",accelerator="Ctrl+S",command=self.savefile)
    # Adding Save As file Command
    self.filemenu.add_command(label="Save As",accelerator="Ctrl+A",command=self.saveasfile)
    # Adding Seprator
    self.filemenu.add_separator()
    # Adding Exit window Command
    self.filemenu.add_command(label="Exit",accelerator="Ctrl+E",command=self.exit)
    # Cascading filemenu to menubar
    self.menubar.add_cascade(label="File", menu=self.filemenu)

    # Creating Edit Menu
    self.editmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding Cut text Command
    self.editmenu.add_command(label="Cut",accelerator="Ctrl+X",command=self.cut)
    # Adding Copy text Command
    self.editmenu.add_command(label="Copy",accelerator="Ctrl+C",command=self.copy)
    # Adding Paste text command
    self.editmenu.add_command(label="Paste",accelerator="Ctrl+V",command=self.paste)
    # Adding Seprator
    self.editmenu.add_separator()
    # Adding Undo text Command
    self.editmenu.add_command(label="Undo",accelerator="Ctrl+Z",command=self.undo)
    # Cascading editmenu to menubar
    self.menubar.add_cascade(label="Edit", menu=self.editmenu)

    # Creating Help Menu
    self.helpmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    # Adding About Command
    self.helpmenu.add_command(label="About",command=self.infoabout)
    # Cascading helpmenu to menubar
    self.menubar.add_cascade(label="Help", menu=self.helpmenu)

    self.runmenu = Menu(self.menubar,font=("times new roman",12,"bold"),activebackground="skyblue",tearoff=0)
    self.menubar.add_cascade(label="Run Files", menu=self.runmenu)
    self.runmenu.add_command(label="Run File",accelerator="CTRL + F5 (Or not Due to python being annoying)",command=run)
    self.runmenu.add_command(label="Install PYinstaller",accelerator="Requires Python (And python scripts folder in path.)",command=installPYIN)
    self.runmenu.add_command(label="Compile",accelerator="Requires Python PYinstaller (And python scripts folder in path.)",command=compiler)
    self.runmenu.add_command(label="About Pyinstaller",command=self.pyin)
    # Creating Scrollbar
    scrol_y = Scrollbar(self.root,orient=VERTICAL)
    # Creating Text Area
    self.txtarea = Text(self.root,yscrollcommand=scrol_y.set,font=("times new roman",Fsize,"bold"),state="normal",relief=GROOVE)
    # Packing scrollbar to root window
    scrol_y.pack(side=RIGHT,fill=Y)
    # Adding Scrollbar to text area
    scrol_y.config(command=self.txtarea.yview)
    #if mode == 'Black':
    #  self.scrol_y.configure(background='#1a1a1a',fg='#f0f0f5')
    # Packing Text Area to root window
    self.txtarea.pack(fill=BOTH,expand=1)
    if mode == 'Black':
      self.txtarea.configure(background='black',fg='#f0f0f5')
    if mode == 'Gray':
      self.txtarea.configure(background='#737373',fg='#f0f0f5')
    
    def syn(txtarea,event=None,):
      txtarea.mark_set("range_start", "1.0")
      data = txtarea.get("1.0", "end-1c")
      for token, content in lex(data, PythonLexer()):
        txtarea.mark_set("range_end", "range_start + %dc" % len(content))
        txtarea.tag_add(str(token), "range_start", "range_end")
        txtarea.mark_set("range_start", "range_end")

    def tab(text):
      print("tab pressed")
      text.insert(INSERT, "    ")
      #return 'break'
    # Binding Ctrl+n to newfile funtion
    self.txtarea.bind("<Control-n>",self.newfile)
    # Binding Ctrl+o to openfile funtion
    self.txtarea.bind("<Control-o>",self.openfile)
    # Binding Ctrl+s to savefile funtion
    self.txtarea.bind("<Control-s>",self.savefile)
    # Binding Ctrl+a to saveasfile funtion
    self.txtarea.bind("<Control-a>",self.saveasfile)
    # Binding Ctrl+e to exit funtion
    self.txtarea.bind("<Control-e>",self.exit)
    # Binding Ctrl+x to cut funtion
    self.txtarea.bind("<Control-x>",self.cut)
    # Binding Ctrl+c to copy funtion
    self.txtarea.bind("<Control-c>",self.copy)
    # Binding Ctrl+v to paste funtion
    self.txtarea.bind("<Control-v>",self.paste)
    # Binding Ctrl+u to undo funtion
    self.txtarea.bind("<Control-u>",self.undo)
    #self.txtarea.bind("<Control-F5>", run)
    self.txtarea.bind("<KeyRelease>", syn(self.txtarea))
    #self.txtarea.bind("<a>", tab(self.txtarea))
    #self.txtarea.bind('<Control-F5>', run())
    #737373
    # Calling shortcuts funtion
    self.shortcuts()

  # Defining settitle function
  def settitle(self):
    # Checking if Filename is not None
    if self.filename:
      # Updating Title as filename
      self.title.set(self.filename)
    else:
      # Updating Title as Untitled
      self.title.set("Untitled")

  # Defining New file Function
  def newfile(self,*args):
    # Clearing the Text Area
    self.txtarea.delete("1.0",END)
    # Updating filename as None
    self.filename = None
    # Calling settitle funtion
    self.settitle()
    # updating status
    self.status.set("New File Created")

  # Defining Open File Funtion
  def openfile(self,*args):
    # Exception handling
    try:
      # Asking for file to open
      self.filename = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      # checking if filename not none
      if self.filename:
        # opening file in readmode
        infile = open(self.filename,"r")
        # Clearing text area
        self.txtarea.delete("1.0",END)
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing the file	
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Opened Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Save File Funtion
  def savefile(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Reading the data from text area
        data = self.txtarea.get("1.0",END)
        # opening File in write mode
        outfile = open(self.filename,"w")
        # Writing Data into file
        outfile.write(data)
        # Closing File
        outfile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Saved Successfully")
      else:
        self.saveasfile()
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Save As File Funtion
  def saveasfile(self,*args):
    # Exception handling
    try:
      # Asking for file name and type to save
      untitledfile = filedialog.asksaveasfilename(title = "Save file As",defaultextension=".txt",initialfile = "Untitled.txt",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
      # Reading the data from text area
      data = self.txtarea.get("1.0",END)
      # opening File in write mode
      outfile = open(untitledfile,"w")
      # Writing Data into file
      outfile.write(data)
      # Closing File
      outfile.close()
      # Updating filename as Untitled
      self.filename = untitledfile
      # Calling Set title
      self.settitle()
      # Updating Status
      self.status.set("Saved Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining Exit Funtion
  def exit(self,*args):
    op = messagebox.askyesno("WARNING","Your Unsaved Data May be Lost!!")
    if op>0:
      self.root.destroy()
    else:
      return

  # Defining Cut Funtion
  def cut(self,*args):
    self.txtarea.event_generate("<<Cut>>")

  # Defining Copy Funtion
  def copy(self,*args):
      		self.txtarea.event_generate("<<Copy>>")

  # Defining Paste Funtion
  def paste(self,*args):
    self.txtarea.event_generate("<<Paste>>")

  # Defining Undo Funtion
  def undo(self,*args):
    # Exception handling
    try:
      # checking if filename not none
      if self.filename:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # opening File in read mode
        infile = open(self.filename,"r")
        # Inserting data Line by line into text area
        for line in infile:
          self.txtarea.insert(END,line)
        # Closing File
        infile.close()
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
      else:
        # Clearing Text Area
        self.txtarea.delete("1.0",END)
        # Updating filename as None
        self.filename = None
        # Calling Set title
        self.settitle()
        # Updating Status
        self.status.set("Undone Successfully")
    except Exception as e:
      messagebox.showerror("Exception",e)

  # Defining About Funtion
  def infoabout(self):
    messagebox.showinfo("About NoteBook","A Simple Text Editor\nCreated by Codespeedy.com\n Edited By R2boyo25.")
  def pyin(self):
    messagebox.showinfo("Pyinstaller","A Program Used By Python to make .exe filese\nHelp1:https://pyinstaller.readthedocs.io/en/stable/usage.html\nHelp2:https://stackoverflow.com/questions/45951964/pyinstaller-is-not-recognized-as-internal-or-external-command")
    #messagebox.insert('Pyinstaller', "link", HyperLinkManager.add('https://pyinstaller.readthedocs.io/en/stable/usage.html'))
    #messagebox.insert('Pyinstaller', "link", HyperlinkManager.add('click2'))
    #messagebox.showinfo()
  #run=run()
  # Defining shortcuts Funtion
  def shortcuts(self):
    return 'no'
    # Binding Ctrl+n to newfile funtion
    self.txtarea.bind("<Control-n>",self.newfile)
    # Binding Ctrl+o to openfile funtion
    self.txtarea.bind("<Control-o>",self.openfile)
    # Binding Ctrl+s to savefile funtion
    self.txtarea.bind("<Control-s>",self.savefile)
    # Binding Ctrl+a to saveasfile funtion
    self.txtarea.bind("<Control-a>",self.saveasfile)
    # Binding Ctrl+e to exit funtion
    self.txtarea.bind("<Control-e>",self.exit)
    # Binding Ctrl+x to cut funtion
    self.txtarea.bind("<Control-x>",self.cut)
    # Binding Ctrl+c to copy funtion
    self.txtarea.bind("<Control-c>",self.copy)
    # Binding Ctrl+v to paste funtion
    self.txtarea.bind("<Control-v>",self.paste)
    # Binding Ctrl+u to undo funtion
    self.txtarea.bind("<Control-u>",self.undo)
    #self.txtarea.bind("<Control-F5>", run)
    self.txtarea.bind("<KeyRelease>", syn())
    self.txtarea.bind('<Control-F5>', self.run)




# Creating TK Container
root = Tk()

#
# Passing Root to TextEditor Class
TextEditor(root)
# Root Window Looping

root.mainloop()