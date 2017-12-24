import tkinter as tk
from tkinter import Menu
from tkinter import Label
from tkinter import Entry
from tkinter import Button
from tkinter import Toplevel
from tkinter import LEFT
from tkinter import YES
from tkinter import Frame
from tkinter import Scrollbar
from tkinter import Text
from tkinter import RIGHT
from tkinter import Y
from tkinter import END



import random

global NameEntry
global BranchEntry
global RandomNumberEntry

def GetBranchCode(Roll):
		Roll=Roll[2:4]
		BCode=''
		if Roll == '01': BCode='075.'
		if Roll == '02': BCode='076.'
		if Roll == '03': BCode='065.'
		if Roll == '04': BCode='066.'
		if Roll == '05': BCode='062.'
		if Roll == '06': BCode='067.'
		if Roll == '07': BCode='068.'
		if Roll == '08': BCode='069.'
		if Roll == '09': BCode='070.'
		if Roll == '11': BCode='077.'
		if Roll == '12': BCode='063.'
		if Roll == '13': BCode='071.'
		if Roll == '14': BCode='072.'
		if Roll == '15': BCode='073.'
		if Roll == '16': BCode='074.'
		if Roll == '17': BCode='064.'
		return BCode

def bynamepushed():
	global NameEntry
	
	txt=NameEntry.get()
	if not txt: 
		message=Toplevel()
		Label(message,text="Invalid Details",justify=LEFT).pack(expand=YES, padx=10,pady=10)
	else: ByName(txt)
	NameEntry.delete(0,END)

#Search the ProxyList By Name
def ByName(Name):
	#try:
	data=open('resources/data.dat','r')										#opening data file
	#except IOError as e:
	#	message=Toplevel()
	#	Label(message,text="Data File Not Found",justify=LEFT).pack(expand=YES, padx=10,pady=10)
	out=open('result.txt','w')
	Name=Name.upper()
	BranchCode=''
	Record=''													
	counter=0														#counter for the not found result
	while True:
		LineRead=data.readline()									#reading data file line by line
		RollNumber=LineRead[:8]										#Extracting RollNumber
		JEERank=LineRead[9:16]										#Extracting JEERank
		NameinData=LineRead[17:]									#Taking Name in Data for Comparison
		
		if Name in NameinData:
			counter+=1												#Counter for result fouund at least once
			LineRead.rstrip()										#stripping \n fromm the line
			Record=Record+RollNumber+"\t"+NameinData
			BranchCode=GetBranchCode(RollNumber)					#Get BranchCode
			UserID=BranchCode+RollNumber 							#Make UserID	
			Pwd=JEERank+'XYZ'										#Make  Password
			out.write(UserID+'\t'+Pwd+'\n')
		if not LineRead:
			break
	data.close()
	message=Toplevel()
	message.title("Results")
	if not counter:
		out.write('Invalid Details')								#not found case
		Label(message,text="Not Found",justify=LEFT).pack(expand=YES, padx=10,pady=10)
	else:
		ResultFrame=Frame(message,height=100,width=40)
		ResultScroll=Scrollbar(ResultFrame)
		ResultText=Text(ResultFrame)
		ResultScroll.pack(side=RIGHT,fill=Y)
		ResultText.pack(side=LEFT,fill=Y)
		ResultFrame.pack()
		ResultScroll.config(command=ResultText.yview)
		ResultText.config(yscrollcommand=ResultScroll.set)
		ResultText.insert(END,Record+"Check Out Result.txt for Proxy UserID and Password")
	out.close()

def bybranchpushed():
	global BranchEntry
	txt=BranchEntry.get()
	if not txt: 
		message=Toplevel()
		Label(message,text="Invalid Details",justify=LEFT).pack(expand=YES, padx=10,pady=10)
	else: ByBranch(txt)
	BranchEntry.delete(0,END)
	
#Search All the Proxies for a Particular Branch
def ByBranch(BranchTwoDigits):
	#try:
	data=open('resources/data.dat','r')										#opening data file
	#except IOError as e:
	#	message=Toplevel()
	#	Label(message,text="Data File Not Found",justify=LEFT).pack(expand=YES, padx=10,pady=10)
	out=open('result.txt','w')
	BranchCode=''
	Record=''												
	counter=0														#counter for the not found result
	while True:
		LineRead=data.readline()									#reading data file line by line
		RollNumber=LineRead[:8]										#Extracting RollNumber
		JEERank=LineRead[9:16]										#Extracting JEERank
		NameinData=LineRead[17:]									#Taking Name in Data for Comparison
		if str(BranchTwoDigits) in RollNumber[2:4]:
			counter+=1												#Counter for result fouund at least once
			LineRead.rstrip()										#stripping \n fromm the line
			Record=Record+RollNumber+'\t'+NameinData
			BranchCode=GetBranchCode(RollNumber)					#Get BranchCode
			UserID=BranchCode+RollNumber 							#Make UserID	
			Pwd=JEERank+'XYZ'										#Make  Password
			out.write(UserID+'\t'+Pwd+'\n')			
		if not LineRead:
			break
	data.close()
	message=Toplevel()
	message.title("Results")
	if not counter:
		out.write('Invalid Details')								#not found case
		Label(message,text="Not Found",justify=LEFT).pack(expand=YES, padx=10,pady=10)
	else:
		ResultFrame=Frame(message,height=100,width=40)
		ResultScroll=Scrollbar(ResultFrame)
		ResultText=Text(ResultFrame)
		ResultScroll.pack(side=RIGHT,fill=Y)
		ResultText.pack(side=LEFT,fill=Y)
		ResultFrame.pack()
		ResultScroll.config(command=ResultText.yview)
		ResultText.config(yscrollcommand=ResultScroll.set)
		ResultText.insert(END,Record+"Check Out Result.txt for Proxy UserID and Password")
	out.close()

def randomlypushed():
	global RandomNumberEntry
	txt=RandomNumberEntry.get()
	if not txt:
		message=Toplevel()
		Label(message,text="Invalid Details",justify=LEFT).pack(expand=YES, padx=10,pady=10)
	else: Randomly(int(txt))
	RandomNumberEntry.delete(0,END)
	
#Search Randomly for N number of Proxies
def Randomly(NProxy):
	#try:
	data=open('resources/data.dat','r')										#opening data file
	#except IOError as e:
	#	message=Toplevel()
	#	Label(message,text="Data File Not Found",justify=LEFT).pack(expand=YES, padx=10,pady=10)
	out=open('result.txt','w')										#opening output File
	Randomlist=[]
	BranchCode=''												
	counter=0
	RandomNumber=0;
	Record=''

	for i in range(NProxy):											#Loop for Getting N Random Numbers
		RandomNumber=random.choice(range(996))
		Randomlist.append(RandomNumber)
	
	while True:
		LineRead=data.readline()									#reading data file line by line
		RollNumber=LineRead[:8]										#Extracting RollNumber
		JEERank=LineRead[9:16]										#Extracting Rank
		NameinData=LineRead[17:]	
		counter+=1													#Counter for Getting N numbered Proxy Data			
		if counter in Randomlist:
			LineRead.rstrip()										#stripping \n fromm the line
			Record=Record+RollNumber+'\t'+NameinData
			BranchCode=GetBranchCode(RollNumber)					#Get BranchCode
			UserID=BranchCode+RollNumber 							#Make UserID	
			Pwd=JEERank+'XYZ'										#Make  Password
			out.write(UserID+'\t'+Pwd+'\n')
		if not LineRead:
			break
	data.close()
	message=Toplevel()
	message.title("Results")
	if not counter:
		out.write('Invalid  Details')								#not found case
		Label(message,text="Not Found",justify=LEFT).pack(expand=YES, padx=10,pady=10)
	else:
		ResultFrame=Frame(message,height=100,width=40)
		ResultScroll=Scrollbar(ResultFrame)
		ResultText=Text(ResultFrame)
		ResultScroll.pack(side=RIGHT,fill=Y)
		ResultText.pack(side=LEFT,fill=Y)
		ResultFrame.pack()
		ResultScroll.config(command=ResultText.yview)
		ResultText.config(yscrollcommand=ResultScroll.set)
		ResultText.insert(END,Record+"Check Out Result.txt for Proxy UserID and Password")
	out.close()

def ShowInfo():
	message=Toplevel()
	Label(message,text="Made With Love by SSJ",justify=LEFT).pack(expand=YES, padx=10,pady=10)
	
def main():
	global NameEntry
	global BranchEntry
	global RandomNumberEntry
	
	root = tk.Tk() # Create the root (base) window where all widgets go

	root.title("Proxy Program")

	menubar=Menu(root)
	filemenu=Menu(menubar)
	filemenu.add_command(label="About",command=ShowInfo)
	filemenu.add_separator
	filemenu.add_command(label="Exit",command=root.destroy)
	menubar.add_cascade(label="More",menu=filemenu)
	root.config(menu=menubar)
	
	NameLabel = Label(root,text="Name: ")
	NameLabel.grid(padx=10,pady=10,row=1,column=0)
	NameEntry = Entry(root)
	NameEntry.grid(padx=10,pady=10,row=1,column=1)
	NameButton = Button(root, text="Hack Name",command=bynamepushed)
	NameButton.grid(padx=10,pady=5,row=1,column=2)


	BranchLabel = Label(root,text="Branch Two Digits: ")
	BranchLabel.grid(padx=10,pady=10,row=3,column=0)
	BranchEntry = Entry(root)
	BranchEntry.grid(padx=10,pady=10,row=3,column=1)
	BranchButton = Button(root, text="Hack Branch",command=bybranchpushed)
	BranchButton.grid(padx=10,pady=5,row=3,column=2)


	RandomLabel = Label(root,text="Number : ")
	RandomLabel.grid(padx=10,pady=10,row=5,column=0)
	RandomNumberEntry = Entry(root)
	RandomNumberEntry.grid(padx=10,pady=10,row=5,column=1)
	RandomButton = Button(root, text="Hack Randomly",command=randomlypushed)
	RandomButton.grid(padx=10,pady=5,row=5,column=2)

	root.mainloop() # Start the event loop

main()
