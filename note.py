# Modules
from tkinter import *
from tkinter import filedialog

#Variables
GREY = "#101012"
LIGHT_GREY = "#303030"
WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 700

# App
class App():
  # Window setup
  def __init__(self):
    #root
    self.root = Tk()
    self.root.title("Untitled - Notepad")
    self.root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    self.root.configure(bg=GREY)
    self.root.wm_iconbitmap("Notepad.ico")
    #Menus
    self.menubar = Menu(self.root)
    self.root.config(menu=self.menubar)
    self.fileMenu = Menu(self.menubar, tearoff=0)
    self.fileMenu.add_command(label="Save", command=self.SaveFile)
    self.fileMenu.add_command(label="Save as...", command=self.SaveFilesAs)
    self.fileMenu.add_command(label="Open", command=self.Openfiles)
    self.menubar.add_cascade(label="File", menu=self.fileMenu)
    #textarea
    self.TextArea = Text(self.root, bg=GREY, relief="flat", fg="white", font=("Arial", 13), insertbackground="white")
    self.TextArea.pack(expand=True, anchor="nw", fill=BOTH)
    #bindings
    self.TextArea.bind("<Control-s>", self.SaveFile)
    self.TextArea.bind("<Control-o>", self.Openfiles)
    self.TextArea.bind("<Control-a>", self.SaveFilesAs)
    self.root.mainloop()
  
  #save a file as
  def SaveFilesAs(self, event=None):
    self.filename = filedialog.asksaveasfilename(filetypes=[('All files', '*')])
    if self.filename:
      self.root.title(self.filename)
      TextAreaText = self.TextArea.get("1.0", END)
      f = open(self.filename, 'w', encoding="utf8")
      f.write(TextAreaText)
      f.close()

  # open a file
  def Openfiles(self, event=None):
    self.filename = filedialog.askopenfilename(title="Choose a file", filetypes=[('All files', '*')])
    if self.filename == "":
      pass
    else:
      f = open(self.filename, "r", encoding="utf8")
      self.TextArea.delete('1.0', END)
      self.TextArea.insert(INSERT, f.read())
      self.root.title(self.filename)
      f.close()

  #save a file
  def SaveFile(self, event=None):
    try:
      TextAreaText = self.TextArea.get("1.0", END)
      f = open(self.filename, 'w', encoding="utf8")
      f.write(TextAreaText)
      f.close()
      self.root.title(self.filename)
    except NameError:
      pass
    except AttributeError:
      self.filename = filedialog.asksaveasfilename(filetypes=[('All files', '*')])
      if self.filename:
        self.root.title(self.filename)
        TextAreaText = self.TextArea.get("1.0", END)
        f = open(self.filename, 'w', encoding="utf8")
        f.write(TextAreaText)
        f.close()
      
# Calling the app
if __name__ == "__main__":
  Notepad = App()
