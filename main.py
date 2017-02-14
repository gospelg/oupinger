import socket
from time import sleep

#identifies the txt file with the list of computers to resolve
the_file = raw_input('Where is the file with the list of computers to test? \n')

#this is the file that contains the computers that did not match the ip pattern
out_file = 'wrongoucomputers.txt'

#this file is the list of computers whose dns name could not be resolved
err_file = 'couldnotresolve.txt'

#this asks the user what ip pattern they would like to match. 
bingo = raw_input("What ip case would you like to match? (anything that does not contain this string will be flagged) \n")

#opens the file and adds each line to a list
with open(the_file, 'r') as f:
	la_lista = f.read().splitlines()
	

#resolves the dns name for a certain index of the list. Checks to see if the pattern is contained in the ip address it resolved
def checker(x):
	try:
		dog = socket.gethostbyname(la_lista[x])
		if bingo not in dog:
			with open(out_file, 'a') as g:
				g.write(la_lista[x] + '\n')
		else:
			pass
			
	except:
		with open(err_file, 'a') as k:
				k.write(la_lista[x] + ' could not find host address for this one \n')
		 
		

#calls checker on every index in la_lista	
for i in range(len(la_lista)):
	checker(i)
	
print 'Your files are in whatever directory cmd is running in now.'
sleep(20) 
	


			
			
