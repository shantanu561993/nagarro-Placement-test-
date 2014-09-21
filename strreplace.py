#!/usr/bin/env python


def foo(a,b,c):
	mylist=list(a.split())
	x=mylist.index(b)
	y=mylist.index(c)
	mylist[x]=c
	mylist[y]=b
	print " ".join(mylist)
	


if __name__=='__main__':
	a=raw_input("Enter String: ")
	b=raw_input("Enter word to be replaced: ")
	c=raw_input("Enter Word to be replaced with: ")
	foo(a,b,c)	
