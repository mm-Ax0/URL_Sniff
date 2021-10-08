#!usr/bin/python3

import urllib.request #the import that acutally allows the request to happen
import sys
import argparse #customize your args
import subprocess
import os

def helpme():
	print ("Syntax: -u <url> -f <wordlist.txt> -m <Preferred mode>\n")
	print ("Usage: This Program acts as a fuzzer allowing you to enumerate unseen pages from targets. The program takes the given url and tests the entered url against file paths or extensions.")
	print ("Available Modes:\n")
def main():
	
	parser = argparse.ArgumentParser(description='Url Fuzzing tool')
	parser.add_argument('-m', '--m', help='Mode',type=str,required=False)
	parser.add_argument('-x', '--x', help='Extension mode',type=str,required=False)
	parser.add_argument('-f','--f', help='Source file',type=str,required=False)
	parser.add_argument('-u','--u', help='Url Target',type=str,required=False)
	args = vars(parser.parse_args()) 	

	arguments = len(sys.argv) #this turns the arguments into a fixed #, that # being the length
	if (arguments < 2):
		helpme()
	elif (arguments >= 2):
			urlsniff(args['u'], args['f'], args['m'])
	
	else: 
		print("Uknown Error..")
		

def urlsniff(url,wordlist,stylemode):#this function works with the url

	scopecodes=[301,302,307,200,204]
	print("-Checking Original Url-")
	try:
		checks = urllib.request.urlopen(url).getcode() #checks initial url.
		print("[+]Active[+] ->",url,":",checks)
		#fileDir = os.path.dirname(os.path.realpath('__file__')) #print current DIR of file.
		fileObj = open(wordlist, "r") #opens source file in read mode.
	except Exception as err:
			print(f'[-]Inactive[-] -> {url} : {str(err)}\n')
			sys.exit()
	print("-"*60)	
	if stylemode == "vv":
		for content in fileObj:
			target = url+"/"+content
			str(target) #make target a string.
		
			try:	
				maincode = (urllib.request.urlopen(target).getcode())
				if (maincode == scopecodes[3]):
					print ( "[+]Active[+] ->",target,":",maincode)
					print("-"*60)
				else:
					print(target, "Code:", maincode)
					print("-"*60)
			except Exception as code:
				print(f'[-]Inactive[-] -> {target} : {str(code)}\n')
				print("-"*60)
		
	else:
		for content in fileObj:
			target = url+"/"+content
			str(target) #make target a string.
		
			outofscope=[]
			try:
				maincode = (urllib.request.urlopen(target).getcode())
				if (maincode in scopecodes):
					print(target, "Code:", maincode)
					print("-"*60)
				
				else:
					print("[-]This code is not in scopecodes[-]")
			except Exception as code:
				outofscope.append(code)
		
		
subprocess.run('python3 Banner.py', shell=True) #'banner grab'
main()
