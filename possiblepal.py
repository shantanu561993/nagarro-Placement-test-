#!/usr/bin/env python

def foo(teststr):
	dictstr={}
	count=0
	for item in teststr:
		if dictstr.has_key(item):
			dictstr[item]+=1
		else:
			dictstr[item]=1
	if len(teststr)%2==0:
		for item in disctstr.itervalues():
			if(item%2==0):
				return False
		return True
	else:
		for item in dictstr.itervalues():
			if count>1:
				return False
			if(item%2!=0):
				count+=1
		return True
		




if __name__=='__main__':
	if(foo(list(raw_input("Enter Test String: ")))):
		print "Possible Palindrome"
	else:
		print "Not a poosible palindrome"
