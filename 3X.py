import random

#Get BracnhCode for the UserID
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

#Search By Name
def ByName():														
	data=open('resources/data.dat','r')										#opening data file
	out=open('result.dat','w')										#Opening Output File
	Name=input('Enter Name:')										#Input  Name
	Name=Name.upper()
	BranchCode=''													
	counter=0														#counter for the not found result
	while True:
		LineRead=data.readline()									#reading data file line by line
		RollNumber=LineRead[:8]										#Extracting RollNumber
		JEERank=LineRead[9:16]										#Extracting JEERank
		NameinData=LineRead[17:]									#Taking Name in Data for Comparison
		
		if Name in NameinData:
			counter+=1												#Counter for result fouund at least once
			LineRead.rstrip()										#stripping \n fromm the line
			print (LineRead[:16],'\t',LineRead[17:])
			BranchCode=GetBranchCode(RollNumber)					#Get BranchCode
			UserID=BranchCode+RollNumber 							#Make UserID	
			Pwd=JEERank+'XYZ'										#Make  Password
			out.write(UserID)										#Write Output in output file
			out.write('\t')
			out.write(Pwd)
			out.write('\n')
		if not LineRead:
			break
				
	if not counter:print ('Not Found')								#not found case
	data.close()
	out.close()

#Search All the Proxies for a Particular Branch
def ByBranch():														
	data=open('resources/data.dat','r')										#opening data file
	out=open('result.dat','w')
	BranchTwoDigits=input("Enter the two digits from roll number which identify a branch\n")
	BranchCode='072.'												#BranchCode for UserID. For now take the branch code as 072
	counter=0														#counter for the not found result
	while True:
		LineRead=data.readline()									#reading data file line by line
		RollNumber=LineRead[:8]										#Extracting RollNumber
		JEERank=LineRead[9:16]										#Extracting Rank
		if str(BranchTwoDigits) in RollNumber[2:4]:
			counter+=1												#Counter for result found at least once
			BranchCode=GetBranchCode(RollNumber)					#GetBranchCode
			UserID=BranchCode+RollNumber 							#Make UserID
			Pwd=JEERank+'XYZ'										#Make Password
			print (LineRead[:16],'\t',LineRead[17:])
			out.write(UserID)										#Write Output in output file
			out.write('\t')
			out.write(Pwd)
			out.write('\n')
		if not LineRead:
			break

	if not counter:print ('Not Found')								#not found case
	data.close()
	out.close()

#Search Randomly for N number of Proxies
def Randomly():														
	data=open('resources/data.dat','r')										#opening data file
	out=open('result.dat','w')										#opening output File
	NProxy=input("Enter \'N\'\n")
	Randomlist=[]
	BranchCode='072.'												
	counter=0
	RandomNumber=0;

	for i in range(int(NProxy)):											#Loop for Getting N Random Numbers
		RandomNumber=random.choice(range(996))
		Randomlist.append(RandomNumber)
	
	while True:
		LineRead=data.readline()									#reading data file line by line
		RollNumber=LineRead[:8]										#Extracting RollNumber
		JEERank=LineRead[9:16]										#Extracting Rank
		counter+=1													#Counter for Getting N numbered Proxy Data			
		if counter in Randomlist:
			BranchCode=GetBranchCode(RollNumber)					#Get Branch Code
			UserID=BranchCode+RollNumber 							#Make UserID
			Pwd=JEERank+'XYZ'										#Make Password
			print (LineRead[:16],'\t',LineRead[17:])
			out.write(UserID)										#Write Output to Output File
			out.write('\t')
			out.write(Pwd)
			out.write('\n')
		if not LineRead:
			break

	if not counter:print ('Not Found')								#not found case
	data.close()
	out.close()

#Asking for choice, how the user wants to search
choice=input("Choose How You want to Search:\n1. By Name\n2. By Branch\n3. Randomly \'n\' numbers of proxy\n")

if choice=='1':
	ByName()

elif choice=='2':
	ByBranch()

elif choice=='3':
	Randomly()
