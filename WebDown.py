from Tkinter import *
from tkMessageBox import *
from ttk import *
import subprocess
class first:
	def __init__(self,root):
		root.title("WebDown")
		root.geometry("1024x500+0+0")
		root.configure(background="black")
		self.s=Style()
		self.s.configure("TFrame",background="black")
		self.first=Frame(root)
		self.first.pack()
		self.head=Label(self.first,text="WebDown",foreground="white",
				background="black",font=("arial","50","bold"))
		self.head.pack()
		self.exp=Label(self.first,
			text="A Python GUI Application For wget.",
			font=("helvetica","20"),background="black",
			foreground="white").pack()

		self.by=Label(self.first,text="\nBy : Girish Thakwani Productions",
			foreground="white",background="black",
			font=("arial","16"))
		self.by.pack()
		self.info1=Label(self.first,foreground="white",background="black",
			font=("arial","18","italic"),text="\n\nWget is extremely powerful, but like with most other command line programs, the number").pack()
		self.info2=Label(self.first,foreground="white",background="black",font=("arial","18","italic"),
			text="of complex options it supports can be intimidating to new users. Thus what we have here").pack()
		self.info3=Label(self.first,foreground="white",background="black",font=("arial","18","italic"),
			text="are a collection of wget commands that you can use to accomplish common tasks from ").pack()
		self.info4=Label(self.first,foreground="white",background="black",font=("arial","18","italic"),
			text="downloading single files to mirroring entire websites.\n\n\n").pack()
			
		self.second=Frame(root)
		self.second.pack()
		self.button1=Button(self.second,text="Direct Options",command=nextdi).pack()
		#self.button2=Button(self.second,text="Developer Options",command=nextde).pack()


def main():
	master=Tk()
	fir=first(master)
	master.mainloop()

def nextdi():
		subprocess.call(["python","start.py"])
def nextde():
		subprocess.call(["python","start2.py"])
if __name__ == '__main__':
	main()
