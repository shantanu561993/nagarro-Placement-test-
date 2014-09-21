#!/usr/bin/env python

def foo(a):
	c=[]
	for i in xrange(len(a)):
		if ((0 in a) and (i%2==0 or ( 1 not in a))):
			c.append(0)
			a.remove(0)

		elif ((1 in a) and (i%2!=0 or ( 0 not in a))):
			c.append(1)
			a.remove(1)
		print c[i],




if __name__=='__main__':
	foo(map(int,raw_input()))
