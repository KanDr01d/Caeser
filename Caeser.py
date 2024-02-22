import secrets,os
from os import name
from time import sleep

#Clear shit in ur terminal
def clear(): 
  
    #Windows 
    if name == 'nt': 
        _ = os.system('cls') 
  
    #Linux, Unix & Mac
    else: 
        _ = os.system('clear')

#Latin Alphabelt (both uppercase and lowercase), 26 chars
LowAlpha = "abcdefghijklmnopqrstuvwxyz"
UpAlpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Input custom string
def CustomString():
	global UpAlpha, LowAlpha, NewAlpha
	def TryAgain():
		sleep(2)
		clear()
		CustomString()

	String = str(input("Do you use custom alphabet string? (Y/N): ").upper())
	if String == "N":
		pass
	elif String == "Y":
		NewAlpha = str(input("Input custom string: ").lower())
		if NewAlpha.isalpha() is not True:
			print ("Invalid string: Only Alphabet string alowed.")
			TryAgain()
		else:
			if len(NewAlpha) > len(LowAlpha) or len(NewAlpha) < len(UpAlpha):
				print ("Invalid string: Your string have ",len(NewAlpha),(". Only 26 character strings are allowed"))
				TryAgain()
			else:
				for Checker in range(len(NewAlpha)):
					if NewAlpha[Checker] in LowAlpha:
						Count = NewAlpha.count(NewAlpha[Checker])
						if Count > 1:
							print ("Ay, you seen to have",Count, NewAlpha[Checker], "in your string. What do you suppose me to do with your step-mum?")
							print ("Check your string carefully!")
							TryAgain()
						elif Count == 0:
							print ("Ay, you seen to have",Count, NewAlpha[Checker], "in your string. What do you suppose me to do with your missing-mum?")
							print ("Check your string carefully!")
							TryAgain()
						else:
							pass
			LowAlpha = NewAlpha.lower()
			UpAlpha = NewAlpha.upper()
	else:
		print ("SyntaxError: Unknow command")
		TryAgain()

#Encrypt program
def encrypt(original):
	crypttext = ""
	CustomString()
	for char in original:
		if char in LowAlpha:
			encrypttext = (LowAlpha.find(char) + Key) % 26
			crypttext += LowAlpha[encrypttext]
		elif char in UpAlpha:
			encrypttext = (UpAlpha.find(char) + Key) % 26
			crypttext += UpAlpha[encrypttext]
		else:
			crypttext += char
	return crypttext

#Encrypt screen
def EncryptScreen():
	original = input("Enter the text you want to be encrypt: ")
	SA(str)
	if Shift == "I":
		IK()
	elif Shift == "R":
		RKG()
	else:
		print ("Error: Can't identified. Please press again")
		SA(str)
		encrypt(original)
	print ("So your encryped message is",encrypt(original), "and your key is",Key ,". If you want to decrypt that message, use the key to decrypt it.")
	return 1

#Decrypt key (or DeKey)
def DeKey():
	global WIYK
	WIYK = input ("Enter the original key or use key detector? (O - Original key / K - Key detector): ").upper()
	return WIYK

#Decrypt program
def decrypt (original):
	global Key
	global cryptext
	crypttext = ""
	
#Brute Force mode
	if WIYK == "K":
		for Key in range (1,26):
			for char in original:
				if char in LowAlpha:
					decrypttext = (LowAlpha.find(char) - Key) % 26
					crypttext += LowAlpha[decrypttext]
				elif char in UpAlpha:
					decrypttext = (UpAlpha.find(char) - Key) % 26
					crypttext += UpAlpha[decrypttext]
				else:
					crypttext += char
			print ("The original text is: ",crypttext,"and the cryptic key is: ", Key)
			crypttext = ""
			Key = ""
			
#Original mode
	elif WIYK == "O":
		for char in original:
			if char in LowAlpha:
				decrypttext = (LowAlpha.find(char) - Key) % 26
				crypttext += LowAlpha[decrypttext]
			elif char in UpAlpha:
				decrypttext = (UpAlpha.find(char) - Key) % 26
				crypttext += UpAlpha[decrypttext]
			else:
				crypttext += char
		print ("The original text is: ",crypttext,"and the cryptic key is: ",Key)	
	return crypttext

#Decrypt screen
def DecryptScreen():
	original = input ("Enter the text you want to be decrypt: ")
	CustomString()
	DeKey()
	if WIYK == "O":
		IK()
		decrypt(original)
	elif WIYK == "K":
		decrypt(original)
	
#Random Key Generator (or RKG)
def RKG():
	global Key
	Key = secrets.randbelow(26)


#Import key (or IK)
def IK():
	global Key
	print (" Remember: Key limit: 0 < [Your key] < 26 ")
	Import = int(input("Press your key: "))
	while Import > 25 or Import < 1:
		print ("Error: Your key is not valid. Please choose another key.")
		Import = int(input("Press your key: "))
	else:
		Key = Import
	return Key	

#Shift Amount (or SA)
def SA(str):
	global Shift
	Shift = input("Do you want to input your own key or use random key generator (Press I or R to continue)?: ")
	return Shift

#Program menu screen
def Menu(str):
	global MenuOpt
	clear()
	print("Caesar Cipher Encode and Decode program \n")
	print ("encrypt					Encode your text to Caesar")
	print ("decrypt					Decode the Caesar message to normal text")
	print ("exit            			I dont think we need to explain about this one \n")
	MenuOpt = input(">>	").lower()
	if MenuOpt == ("encrypt") or MenuOpt == ("en"):
		EncryptScreen()
		exit(0)
	elif MenuOpt == ("decrypt") or MenuOpt == ("de"):
		DecryptScreen()
		exit(0)
	elif MenuOpt == "exit" or MenuOpt == ("e"):
		exit(0)
	else:
		print ("Syntax Error: Not know command.")
		sleep(1)
		clear()
		Menu(str)

Menu(str)
