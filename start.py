# -*- coding: utf-8 -*-
from Tkinter import *
from tkMessageBox import *
from ttk import *
import subprocess
import os
from tkFileDialog import *
class first:
	def __init__(self,root):
		root.title("WebDown")
		root.geometry("1024x500+0+0")
		root.configure(background="black")
		self.s=Style()
		self.s.configure("TFrame",background="black")
		self.s.configure("TCombobox",background="white")
		self.first=Frame(root)
		self.first.pack()
		self.head=Label(self.first,text="WebDown",foreground="white",background="black",font=("arial","30","bold")).pack()
		self.second=Frame(root).pack()
		self.by=Label(self.second,text="\nChoose the options that you want to wget :\n\n",foreground="white",background="black",
			font=("helvetica","16")).pack()
		self.options=StringVar()
		self.list=Combobox(self.second,textvariable=self.options,width="70",height="30",values=("Download a single file from the Internet",
			"Download an entire website including all the linked pages and files",
			"Download all the MP3 files from a sub directory",
			"Download all images from a website",
			"Download the PDF documents from a website",
			"Download all files from a website but exclude a few directories",
			"Find the size of a file without downloading it (look for Content Length in the response, the size is in bytes)",
			"Download a web page with all assets"),font="2").pack()
		self.options.set("Download an entire website including all the linked pages and files")
		self.emp=Label(self.second,text="\n\n\n\n\n\n\n\n",background="black").pack()
		self.third=Frame(root).pack()
		self.site=StringVar()
		self.label1=Label(self.third,text="Enter the URL :\n",font=("arial","16"),background="black",foreground="white").pack()
		self.webent=Entry(self.third,textvariable=self.site,width="60",font="2").pack()
		self.free=Label(self.third,text="\n\n",background="black").pack()
		self.fourth=Frame(root).pack()
		self.button1=Button(self.fourth,text="Ok",command=self.bt1).pack()
		self.button2=Button(self.fourth,text="Clear",command=self.clear).pack()
	def bt1(self):
		if self.site.get()=="":
			showinfo(title="Alert",message="Please enter the URL",icon="warning")
		else:
			askyesno(title="WebDown",message="Do you want to continue?")
			if askyesno()==True:
				if self.options.get()=="Download an entire website including all the linked pages and files":
					self.com="wget --limit-rate=200k --no-clobber --convert-links --random-wait -r -p -E -e robots=off -U mozilla "+self.site.get()
					os.system(self.com)
				if self.options.get()=="Download a single file from the Internet":
					self.com="wget"+self.site.get()
					os.system(self.com)
				if self.options.get()=="Download all the MP3 files from a sub directory":
					self.com="wget ‐‐level=1 ‐‐recursive ‐‐no-parent ‐‐accept mp3,MP3 "+self.site.get()
					os.system(self.com)
				if self.options.get()=="Download all images from a websiten folder":
					self.com="wget ‐‐directory-prefix=files/pictures ‐‐no-directories ‐‐recursive ‐‐no-clobber ‐‐accept jpg,gif,png,jpeg "+self.site.get()
					os.system(self.com)
				if self.options.get()=="Download the PDF documents from a website":
					self.com="wget ‐‐mirror ‐‐domains=abc.com,files.abc.com,docs.abc.com ‐‐accept=pdf "+self.site.get()
					os.system(self.com)
				if self.options.get()=="Download all files from a website but exclude a few directories":
					self.com="wget ‐‐recursive ‐‐no-clobber ‐‐no-parent ‐‐exclude-directories "+self.site.get()
					os.system(self.com)
				if self.options.get()=="Find the size of a file without downloading it (look for Content Length in the response, the size is in bytes)":
					self.com="wget ‐‐spider ‐‐server-response"+self.site.get()
					os.system(self.com)
				if self.options.get()=="Download a web page with all assets":
					self.com="wget ‐‐page-requisites ‐‐span-hosts ‐‐convert-links ‐‐adjust-extension "+self.site.get()
					os.system(self.com)
			else:
				return
	def clear(self):
		self.site.set("")

def main():
	master=Tk()
	fir=first(master)
	master.mainloop()

if __name__ == '__main__':
	main()